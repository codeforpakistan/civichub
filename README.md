# CivicHub
A repository of all that's civic and good 

## Requirements
This system is build with Django 4.2 and Bootstrap 5.3
* Python 3.8, 3.9, 3.10, 3.11, and 3.12

## Getting started

1. Clone the repository
```
git clone https://github.com/codeforpakistan/civichub.git
cd civichub
```

2. Create and/or activate your python environment
```
# Linux
python -m pip virtualenv env
source env/bin/activate

# Windows
python -m pip virtualenv env
env\Scripts\activate
```

3. Create environment file for configuration; fill in your own secret key
```
DEBUG=on
SECRET_KEY=
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS='localhost,127.0.0.1'
```

4. Run migrations and seed dummy data
```
python manage.py migrate
python manage.py seed
```
This will create the default superuser as well as generate synthetic test data. 

5. Run server
```
python manage.py runserver
```
