# 0. Install

```
$ pip install virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 manage.py createsuperuser
```

# 1. Start DRF Api

```
$ python3 manage.py runserver
```

# 2. Add apps (users)

With `manage.py`:

```
$ python3 manage.py startapp users
```

Or with `django-admin`:

```
$ django-admin startapp users
```
