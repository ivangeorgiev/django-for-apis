# Library Application

## Prepare Environment

```bash
$ py -m venv .venv
$ soruce .venv/Scripts/activate
$ pip install -r requirements-dev.txt
```

For Development Configuration, check out [Django Debug Toolbar during Development](https://ig-gems.readthedocs.io/en/latest/python/django/010-using-django-debug-toolbar-development-only.html).

## Test the Application

```bash
python manage.py test
```

## Serve using Django Development Server

```bash
$ DJANGO_SETTINGS_MODULE=django_project.settings_dev python manage.py runserver
```

## Serve using uvicorn

Make sure that `settings.py` defines `ALLOWED_HOSTS`. If not, the server will respond with _'400 Bad Request'_.

```python
# ...
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# ...
```

The command line is as follows:

```bash
$ pip install uvicorn
$ uvicorn django_project.asgi:application
```

If you want to use `uvicorn` for development and automatically reload when `.py` files are updated, add the `--reload` command line option. For more info see the [uvicorn documentation](https://www.uvicorn.org/settings/#development).
