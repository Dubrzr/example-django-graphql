## Création virtualenv

```
virtualenv -p python3 venv
source venv/bin/activate
```

## Installation

```
cd project
./manage.py migrate
./manage.py makemigrations articles
./manage.py migrate articles

```