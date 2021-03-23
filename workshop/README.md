## Install Django and netmiko

```
pip install django netmiko

OR

pip install -r requirements.txt
```

## 1. Creating a project

```
django-admin startproject mysite
```
## 2. Creating frontend and backend app
```
python manage.py startapp frontend
python manage.py startapp backend
```

## 3. Add app to INSTALL_APPS in settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend',
    'backend'
]
```
## 4. Edit urls.py

#### apps/urls.py
```
urlpatterns = [
    path('', frontend.views.device_connect),
    path('do/connect', backend.views.connect),
    path('admin/', admin.site.urls),
]
```

## 5. Edit views.py