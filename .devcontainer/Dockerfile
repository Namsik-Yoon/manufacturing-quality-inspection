FROM ghcr.io/astral-sh/uv:0.12.23 AS uv
FROM python:3.12.15-bookworm
COPY --from=uv /uv /uvx /usr/local/bin/
RUN apt-get update && apt-get install -y --no-install-recommends git openssh-client curl \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --uid 1000 --create-home --shell /bin/bash developer
ENV UV_LINK_MODE=copy
USER developer

