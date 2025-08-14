import os
import shutil
import sqlite3
import sys
import glob
from datetime import datetime, timedelta, timezone
from pathlib import Path

def _platform():
    if sys.platform.startswith('win'):
        return 'windows'
    if sys.platform == 'darwin':
        return 'mac'
    return 'linux'

def default_paths():
    home = str(Path.home())
    plat = _platform()
    paths = {
        'chrome': [],
        'edge': [],
        'firefox': [],
    }
    if plat == 'windows':
        local = os.environ.get('LOCALAPPDATA', '')
        roaming = os.environ.get('APPDATA', '')
        paths['chrome'] = [os.path.join(local, r'Google\Chrome\User Data\Default\History')]
        paths['edge']   = [os.path.join(local, r'Microsoft\Edge\User Data\Default\History')]
        paths['firefox'] = glob.glob(os.path.join(roaming, r'Mozilla\Firefox\Profiles\*.default-release\places.sqlite'))
    elif plat == 'mac':
        base = os.path.join(home, 'Library', 'Application Support')
        paths['chrome'] = [os.path.join(base, 'Google', 'Chrome', 'Default', 'History')]
        paths['edge']   = [os.path.join(base, 'Microsoft Edge', 'Default', 'History')]
        paths['firefox'] = glob.glob(os.path.join(base, 'Firefox', 'Profiles', '*.default-release', 'places.sqlite'))
    else:
        paths['chrome'] = [os.path.join(home, '.config', 'google-chrome', 'Default', 'History')]
        paths['edge']   = [os.path.join(home, '.config', 'microsoft-edge', 'Default', 'History')]
        paths['firefox'] = glob.glob(os.path.join(home, '.mozilla', 'firefox', '*.default-release', 'places.sqlite'))
    for k, v in paths.items():
        paths[k] = [p for p in v if os.path.exists(p)]
    return paths

def _copy_for_read(original):
    if not os.path.exists(original):
        raise FileNotFoundError(original)
    tmp = Path(original).with_suffix(Path(original).suffix + '.copy')
    shutil.copy2(original, tmp)
    return str(tmp)

def _chrome_time_to_utc(ts):
    if ts is None:
        return None
    try:
        epoch_start = datetime(1601, 1, 1, tzinfo=timezone.utc)
        dt = epoch_start + timedelta(microseconds=int(ts))
        return dt.astimezone(timezone.utc)
    except Exception:
        return None

def _unix_micro_to_utc(ts):
    if ts is None:
        return None
    try:
        return datetime.fromtimestamp(int(ts) / 1_000_000, tz=timezone.utc)
    except Exception:
        return None

def read_chrome_like(db_path, limit=200):
    db_copy = _copy_for_read(db_path)
    rows = []
    con = sqlite3.connect(db_copy)
    try:
        cur = con.cursor()
        cur.execute(
            '''SELECT urls.url, urls.title, urls.visit_count, urls.last_visit_time
               FROM urls
               ORDER BY last_visit_time DESC
               LIMIT ?''',
            (limit,),
        )
        for url, title, count, ts in cur.fetchall():
            dt = _chrome_time_to_utc(ts)
            rows.append(
                {
                    'url': url,
                    'title': title or '',
                    'visit_count': count or 0,
                    'visited_at_utc': dt.isoformat() if dt else None,
                }
            )
    finally:
        con.close()
        try:
            os.remove(db_copy)
        except Exception:
            pass
    return rows

def read_firefox(db_path, limit=200):
    db_copy = _copy_for_read(db_path)
    rows = []
    con = sqlite3.connect(db_copy)
    try:
        cur = con.cursor()
        cur.execute(
            '''SELECT p.url, p.title, p.visit_count, v.visit_date
               FROM moz_places p
               LEFT JOIN moz_historyvisits v ON p.id = v.place_id
               ORDER BY v.visit_date DESC
               LIMIT ?''',
            (limit,),
        )
        for url, title, count, ts in cur.fetchall():
            dt = _unix_micro_to_utc(ts)
            rows.append(
                {
                    'url': url,
                    'title': title or '',
                    'visit_count': count or 0,
                    'visited_at_utc': dt.isoformat() if dt else None,
                }
            )
    finally:
        con.close()
        try:
            os.remove(db_copy)
        except Exception:
            pass
    seen = set()
    dedup = []
    for r in rows:
        if r['url'] in seen:
            continue
        seen.add(r['url'])
        dedup.append(r)
    return dedup[:limit]

def fetch_history(browser='auto', path=None, limit=200):
    if path and os.path.exists(path):
        if browser == 'firefox' or path.endswith('places.sqlite'):
            return read_firefox(path, limit=limit)
        else:
            return read_chrome_like(path, limit=limit)
    paths = default_paths()
    ordered = ['chrome', 'edge', 'firefox'] if browser == 'auto' else [browser]
    for b in ordered:
        for p in paths.get(b, []):
            try:
                if b == 'firefox' or p.endswith('places.sqlite'):
                    return read_firefox(p, limit=limit)
                else:
                    return read_chrome_like(p, limit=limit)
            except Exception:
                continue
    return []
