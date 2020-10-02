
FROM python:3.8-alpine as builder

WORKDIR /app

ENV PATH="/root/.poetry/bin:$PATH"

RUN  set -ex \
	&& apk add --no-cache --virtual .build-deps \
		gcc \
		musl-dev \
        openssl-dev \
        libffi-dev \
    && pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.in-project true

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-root --no-dev \
    && apk del .build-deps

# Stage 2
FROM python:3.8-alpine

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 5000
ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0" ] 

COPY ./ ./
COPY --from=builder /app/ ./