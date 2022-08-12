FROM python:3.8.6

RUN pip install --upgrade pip
COPY ./long_memory ./
RUN pip install -r requirements_docker.txt
RUN pip install gunicorn