FROM python:3.11-slim-buster as builder

RUN pip install poetry==1.5

ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV POETRY_CACHE_DIR="/tmp/poetry_cache"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --no-root


FROM python:3.11-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /app

COPY ./ ./

RUN cat ./scripts/web-prestart.sh > /prestart.sh
RUN cat ./scripts/web-start-reload.sh > /start-reload.sh
RUN cat ./scripts/production-web-start.sh > /web-start.sh
RUN cat ./backend/gunicorn_conf.py > /gunicorn_conf.py

CMD ["bash", "/web-start.sh"]
