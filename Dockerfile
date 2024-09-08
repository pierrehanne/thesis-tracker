# First stage: build dependencies with Poetry
FROM python:3.11-slim AS builder
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Second stage: runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
COPY src/ src/
COPY config.yaml ./
CMD ["poetry", "run", "python", "src/thesis_tracker.py"]
