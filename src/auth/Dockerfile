# syntax=docker/dockerfile:1

# Base image.
FROM python:3.12.0rc2

# Set working directory.
WORKDIR /app

## Install Prerequisites ##
# Instilation of some dependences fails when done via `requirements.txt` file, so install manually.
RUN pip3 install --only-binary :all: greenlet
# Automated dependency install.
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Import code.
COPY . .

## Environment Setup ##
ENV FLASK_APP=/app
ENV FLASK_CONFIG_SECRET_KEY="some-secret"
ENV FLASK_CONFIG_DB_LOCATION="sqlite:////app/database.db"
#ENV FLASK_DEBUG=1

## Launch ##
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

