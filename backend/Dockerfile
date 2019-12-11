#
# ---- Base Node ----
FROM python:3.8.0-buster AS base

# Container info
LABEL description="Backend API"
LABEL maintainer="Taras Protsenko <easylovv@gmail.com>"

# set working directory
WORKDIR /app

# ---- Dependencies ----
FROM base AS deps

# Copy readme & setup.py
RUN mkdir backend
COPY README.md .
COPY setup.py .
# install main requirements
RUN pip install -e . --no-cache-dir

#
# ---- Development dependencies ----
FROM deps AS dev-deps
# install dev requirements
RUN pip install -e .[dev] --no-cache-dir

#
# ---- Development ----
FROM dev-deps AS dev
# set envs
ENV HOST 0.0.0.0
ENV PORT 80
# expose port and define CMD
EXPOSE ${PORT}
# copy app sources
COPY . .
# Ensure entrypoint is executable
RUN chmod +x ./entrypoint.sh

# Entrypoint script to run before any command
ENTRYPOINT ["/app/entrypoint.sh"]
# Default command
CMD backend_launch
