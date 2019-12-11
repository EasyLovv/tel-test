#
# ---- Base Node ----
FROM python:3.8.0-buster AS base

# Container info
LABEL description="Scrapper Worker"
LABEL maintainer="Taras Protsenko <easylovv@gmail.com>"

# set working directory
WORKDIR /app

# ---- Dependencies ----
FROM base AS deps

RUN mkdir -p /usr/share/man/man1 \
    && mkdir -p /usr/share/man/man7 \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y supervisor \
    && apt-get autoclean -y


# Copy readme & setup.py
RUN mkdir scrapper
COPY README.md .
COPY setup.py .
# install main requirements
RUN pip install -e . --no-cache-dir

#
# ---- Development dependencies ----
FROM deps AS dev-deps
# install dev requirements
RUN pip install -e .[dev] --no-cache-dir

# copy app sources
COPY . .
# Ensure entrypoint is executable
#RUN chmod +x ./entrypoint.sh

# Entrypoint script to run before any command
#ENTRYPOINT ["/app/entrypoint.sh"]
