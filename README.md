# WordScheme
## Purpose

WordScheme is a platform for sharing written content. It's designed to help writers of all kinds collaborate and critique each other's work. It can also be used by editors to review work by large groups of people before publication.

## Requirements
### System
1. Python 2.7
2. python-dev
3. postgresql-9.3
4. postgresql-server-dev-9.3
5. python-pip
6. git _(optional)_

### Python libs
_(pip install)_

1. django
2. django-extensions
3. django-filter
4. djangorestframework
5. psycopg2

# Installation
Very basic steps to get up and running. This is **not** a Django security guide.

`$ sudo -u postgres psql postgres -h localhost`

```sql
postgres=# create database wordscheme;
postgres=# create user wsdb with password '<PASSWORD>' login;
postgres=# create database wordscheme;
postgres=# grant all on database wordscheme to wsdb;
postgres=# \q
```

Open `webscheme/settings.py`. Change the following:
* Change `SECRET_KEY`.
* Set `DEBUG` to `False`.

If all goes well, this will get you running with the Django development server.
Webserver configuration is beyond the scope of this document.

```bash
$ ./manage.py migrate
$ ./manage.py runserver <HOST:[PORT]>
```
