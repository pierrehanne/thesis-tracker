# First stage: build dependencies with Poetry
FROM python:3.11-slim AS builder
WORKDIR /app

# Install Poetry in the build stage
RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

# Second stage: runtime
FROM python:3.11-slim
WORKDIR /app

# Install Poetry in the runtime stage
RUN pip install poetry

COPY --from=builder /app /app
COPY src/ src/
COPY config.yaml ./

# Ensure Poetry is in PATH
ENV PATH="/root/.local/bin:$PATH"

CMD ["poetry", "run", "python", "src/thesis_tracker.py"]
