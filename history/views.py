from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .utils import fetch_history, default_paths

def index(request):
    return render(request, 'history/index.html', { 'paths': default_paths() })

def api_history(request):
    browser = (request.GET.get('browser') or 'auto').lower()
    path = request.GET.get('path') or None
    try:
        limit = int(request.GET.get('limit', '200'))
    except ValueError:
        return HttpResponseBadRequest('Invalid limit')
    data = fetch_history(browser=browser, path=path, limit=limit)
    return JsonResponse({ 'results': data, 'count': len(data) })
