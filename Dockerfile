FROM python:3.6.8-alpine

ENV YOUR_ENV=${YOUR_ENV} \ 
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \ 
    PYTHONHASHSEED=random \ 
    PIP_NO_CACHE_DIR=off \ 
    PIP_DISABLE_PIP_VERSION_CHECK=on \ 
    PIP_DEFAULT_TIMEOUT=100 \ 
    POETRY_VERSION=1.0.2

RUN apk --no-cache add \ 
    bash \
    build-base \
    curl \
    gcc \
    gettext \
    git \
    libffi-dev \
    linux-headers \
    openssl \
    musl-dev \
    postgresql-dev \
    tini \ 
    && pip install poetry

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /code

RUN poetry build
RUN pip install dist/onde_dar_sangue-*.whl

ENTRYPOINT ["waitress-serve", "--call", "onde_dar_sangue:start_app"]