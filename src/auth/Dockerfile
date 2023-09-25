# syntax=docker/dockerfile:1

# Base image.
FROM python:3.12.0rc2

# Set working directory.
WORKDIR /app

# Install prerequisites.
RUN pip3 install --only-binary :all: greenlet
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Import code.
COPY . .

# Setup environment.
ENV FLASK_APP=/app
#ENV FLASK_DEBUG=1

# Launch code.
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

