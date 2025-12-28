FROM python:3.9-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache --no-install-project
COPY ./README.md /README.md
COPY ./app ./app
CMD ["uv", "run", "fastapi", "run", "app/main.py", "--port", "8889"]
