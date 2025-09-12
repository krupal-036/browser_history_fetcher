# Browser History Fetcher 🔍

Browser History Fetcher is a modern web application that securely retrieves and displays browsing history from multiple web browsers including Chrome, Edge, Firefox, Opera, and Brave. Built with Django and Bootstrap 5, it provides a responsive interface with data visualization, domain export functionality, and cross-browser compatibility.

---

## ↗️ View the Project
This is a local application designed to run on your machine for privacy and security.

<table align="center" cellspacing="0" cellpadding="0" style="border: none; border-collapse: collapse;">
  <tr>
    <td style="border: none; padding: 0;">
      <img src="https://github.com/user-attachments/assets/6e113319-ade8-4e7d-8203-6b35e2af86d9" alt="Browser Selection Interface" width="1899" height="881" style="display: block; margin: 0; padding: 0; border: none;">
    </td>
  </tr>
  <tr>
    <td style="border: none; padding: 0;">
      <img src="https://github.com/user-attachments/assets/b13331ad-a23e-45c6-a2d7-17963625f975" alt="History Results Table" width="1904" height="469" style="display: block; margin: 0; padding: 0; border: none;">
    </td>
  </tr>
  <tr>
    <td style="border: none; padding: 0;">
      <img src="https://github.com/user-attachments/assets/49634037-848d-468d-aa74-f515a19dc19f" alt="Top Sites Visualization" width="1897" height="997" style="display: block; margin: 0; padding: 0; border: none;">
    </td>
  </tr>
  <tr>
    <td style="border: none; padding: 0;">
      <img src="https://github.com/user-attachments/assets/628699b7-43c9-4071-8628-2ec8de0db0e2" alt="Export Functionality" width="999" height="776" style="display: block; margin: 0; padding: 0; border: none;">
    </td>
  </tr>
  <tr>
    <td style="border: none; padding: 0;">
      <img src="https://github.com/user-attachments/assets/8a035e14-e92d-4d85-85a9-0cf5e4fe70f6" alt="Mobile Responsive View" width="1510" height="558" style="display: block; margin: 0; padding: 0; border: none;">
    </td>
  </tr>
</table>

## ✨ Features
- **Multi-Browser Support:** Retrieves history from Chrome, Edge, Firefox, Opera, and Brave browsers
- **Secure File Handling:** Creates temporary copies of database files to prevent browser locks
- **Interactive Data Visualization:** Displays top 5 most visited sites with interactive elements
- **Export Functionality:** Generates HTML reports of unique domains with copy-to-clipboard features
- **Responsive Design:** Fully optimized for desktop, tablet, and mobile devices
- **Advanced Filtering:** Customizable browser selection, path specification, and result limiting
- **Timestamp Conversion:** Standardizes browser-specific timestamp formats to UTC
- **Modern UI:** Clean, gradient-based design with smooth animations and hover effects

## 🛠️ Technologies Used
- **Backend:** Python 3.9+, Django 4.0+
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Database:** SQLite (for browser history access)
- **UI Framework:** Bootstrap 5
- **Icons:** Bootstrap Icons
- **Python Libraries:** sqlite3, pathlib, datetime, os, shutil

## 📁 Folder Structure
```

# Project Structure

browser_history_fetcher/
├── browser_history_fetcher/          # Main project folder (Django settings & configuration)
│   ├── __init__.py                   # Marks this directory as a Python package
│   ├── asgi.py                       # ASGI config for async deployment
│   ├── settings.py                   # Project-wide settings (database, apps, middleware, etc.)
│   ├── urls.py                       # Root URL routing for the project
│   └── wsgi.py                       # WSGI config for traditional deployment
│
├── history/                          # Main application for browser history fetching
│   ├── templates/                    # HTML templates folder
│   │   └── history/                  # App-specific templates
│   │       └── index.html            # Main template file
│   ├── __init__.py                   # Marks this directory as a Python package
│   ├── admin.py                      # Django admin configuration for models
│   ├── apps.py                       # App-specific configuration
│   ├── models.py                     # Database models for browser history storage
│   ├── urls.py                       # URL routes specific to the history app
│   ├── utils.py                      # Helper/utility functions for history extraction
│   └── views.py                      # View functions (handle requests & responses)
│
├── db.sqlite3                        # Default SQLite database
├── manage.py                         # Django management script (runserver, migrations, etc.)
├── README.md                         # Project documentation
└── requirements.txt                  # Python dependencies for the project

```

## 🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites
- Python 3.7+
- pip (Python package installer)
- Git

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/krupal-036/browser_history_fetcher.git
   cd browser_history_fetcher
   ```

2. **Create and activate a virtual environment:**
   - On macOS and Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Django application:**
   ```bash
   python manage.py runserver
   ```
   
   The application will be available at `http://127.0.0.1:8000/`.

## 👨‍💻 Author
Developed with ❤️ by [Krupal Fataniya](https://github.com/krupal-036).

For any issues or questions, feel free to contact [Krupal ✉️](mailto:krupalfataniya007@gmail.com). 😊