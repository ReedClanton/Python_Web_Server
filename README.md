# python-flask-user-login

# Environment Setup

## Python Virtual Environment

Create Python virtual environment by running the bellow at the repo root:

```sh
python -m venv venv
```

Activate the Python virtual enivronment by sourcing the activate file (as seen bellow):

```sh
. venv/bin/activate
```

Setup virtual environment by installing dependencies:

```sh
pip install flask flask-sqlalchemy flask-login
```

## Configure Environment Variable(s)

```sh
export FLASK_APP=src/auth
export FLASK_DEBUG=1 # Omit for production
```

# Launch Application

```sh
flask run
```
