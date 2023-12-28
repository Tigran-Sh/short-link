FROM python:3.11-slim
# configure pip and python
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=0

# create user and group for the application
RUN groupadd --system --gid 1001 app \
 && useradd --system --create-home --home-dir /app --uid 1001 --gid 1001 app

# upgrade system, install required packages for pip
# remove unused packages, clean apt cache
RUN apt update \
 && apt upgrade -y \
 && apt install -y libpq-dev gcc procps curl zip \
 && apt autoremove -y \
 && apt clean -y \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --chown=1001:1001 requirements.txt .

RUN pip install -r requirements.txt

COPY --chown=1001:1001 . .

USER app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]