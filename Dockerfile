# First stage: build dependencies with Poetry
FROM python:3.11-slim AS builder
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Second stage: runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
COPY src/ src/
COPY config.yaml ./
ENV PATH="/root/.local/bin:$PATH"

# Run the application
CMD ["poetry", "run", "python", "src/thesis_tracker.py"]
