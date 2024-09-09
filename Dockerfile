# First stage: build dependencies with Poetry
FROM python:3.11-slim AS builder
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install

# Second stage: runtime
FROM python:3.11-slim
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /app
COPY --from=builder /app /app
COPY src/ src/
COPY config.yaml ./
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install
RUN poetry run pip list

# Run the application
CMD ["poetry", "run", "python", "src/thesis_tracker.py"]
