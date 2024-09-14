FROM python:3.12-alpine AS build_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR proj

COPY . /proj/


FROM build_app AS dev

ENV PROD 1

RUN poetry install

CMD ["python", "-m", "src.presentation"]
