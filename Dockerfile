FROM python:3.10.4
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD pyproject.toml poetry.lock /app/

RUN apt update
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

ADD . /app

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
