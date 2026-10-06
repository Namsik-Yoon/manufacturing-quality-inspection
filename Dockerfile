FROM ghcr.io/astral-sh/uv:0.12.23 AS uv
FROM python:3.12.15-slim-bookworm
COPY --from=uv /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy PATH="/service/.venv/bin:$PATH" PYTHONUNBUFFERED=1
WORKDIR /service
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
COPY app ./app
RUN uv sync --frozen --no-dev --no-editable && useradd --uid 10001 --create-home inspector
USER inspector
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

