# syntax=docker/dockerfile:1

# I would recommend to use the slim version of Python.
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_NAME=multi-tenant-application
ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY . /app/

CMD ["gunicorn","--bind","0.0.0.0:8000","--timeout","180","multi_tenant_application.wsgi","--workers","2","--threads","4","--worker-class","gthread"]
