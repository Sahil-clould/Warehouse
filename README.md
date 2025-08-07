# Warehouse Management System

This is a Django-based **Warehouse Inventory Management System** that helps manage stock, inventory, and user operations efficiently.

## 🔗 Live Demo

[Click here to view the deployed project on Render](https://warehouse-wg87.onrender.com)

---

## 🛠️ Features


- Add, edit, and delete inventory items
- View item details and filter items
- Dashboard to monitor stock levels
- Responsive frontend using HTML and Bootstrap
- Error handling and form validations

---

## 🚀 Technology Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite3 (default Django DB)
- **Deployment:** Render

---

## 🔧 Setup Instructions

### Clone the repository

```bash
git clone https://github.com/your-username/warehouse-management.git
cd warehouse-management

Create and activate a virtual environment
bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install the requirements
bash
Copy
Edit
pip install -r requirements.txt
Run the development server
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Visit http://localhost:8000 in your browser.

Make sure these settings are applied in settings.py:

python
Copy
Edit
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Use Whitenoise to serve static files
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
Also add Whitenoise to requirements.txt if not present:

txt
Copy
Edit
whitenoise>=6.0.0
And don't forget to run:

bash
Copy
Edit
python manage.py collectstatic
before deploying to Render.



git clone https://github.com/your-username/warehouse-management.git
cd warehouse-management
