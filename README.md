# python-django-training

Python Data Types:-

Text Type:	str  
Numeric Types:	int, float, complex  
Sequence Types:	list, tuple, range  
Mapping Type:	dict  
Set Types:	set, frozenset  
Boolean Type:	bool  
Binary Types:	bytes, bytearray, memoryview  
None Type:	NoneType  

==> def my_function(x, /):
      print(x)
==> ", /" restricts the function only to accept only positional arguments and not allow keyword arguments


# django-project-structure

### ✅ Basic Folder Structure After Running `django-admin startproject myproject`

```
myproject/
│
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app_name/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   └── *.html
│
└── static/
    ├── css/
    ├── js/
    └── images/
```

---

### 📋 What Each File/Folder Does

#### 🔹 `manage.py`

> Command-line utility to interact with the Django project (runserver, migrate, createsuperuser, etc.)

#### 🔹 `myproject/` (inner folder with the same name as your project)

> This is the **project configuration directory**.

* `__init__.py` → Tells Python this is a package.
* `settings.py` → Contains all the settings (DB config, installed apps, static files, etc.)
* `urls.py` → Root URL dispatcher for the project. Routes to individual app URLs.
* `asgi.py` → For async deployments (ASGI = Asynchronous Server Gateway Interface).
* `wsgi.py` → For traditional deployments (WSGI = Web Server Gateway Interface).

---

### 🔹 `app_name/` (You create this with `python manage.py startapp app_name`)

> The actual app where business logic lives.

* `migrations/` → Tracks DB schema changes.
* `admin.py` → Register models here for Django Admin.
* `apps.py` → App configuration (used by Django internally).
* `models.py` → Define your database tables (ORM).
* `views.py` → Logic for handling web requests.
* `urls.py` → Routes for this app (you manually create this).
* `tests.py` → Write unit tests here.

---

### 🔹 `templates/`

> HTML files for rendering dynamic web pages using Django Template Language.

You can have:

```
templates/
├── app_name/
│   └── index.html
```

---

### 🔹 `static/`

> Store static files (CSS, JS, images). Access via `{% static 'path/to/file' %}` in templates.

Structure:

```
static/
├── css/
├── js/
└── images/
```

You must set `STATICFILES_DIRS` in `settings.py` for Django to know where to collect them.

---
