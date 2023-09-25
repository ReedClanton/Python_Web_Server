# Python Web Server

# Run

Applications may be run bia Docker or locally. If you don't know how you should run it, then you should use Docker.

## Docker

To run an application, see the `README.md` file in the application's directory (`<repoRoot>/src/<appName>`).

## Local

### Environment Setup

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

```sh
export FLASK_APP=src/<appName>
```

### Launch Application

From application's directory (`<repoRoot>/src/<appName>`), run:

```sh
python -m flask run --host=0.0.0.0
```
