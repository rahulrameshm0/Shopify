#!/usr/bin/env bash
# Start script used by Render on every boot.
set -o errexit

python manage.py migrate --noinput
python manage.py seed_catalog
python manage.py ensure_superuser

exec gunicorn ecommerce.wsgi:application \
    --bind "0.0.0.0:${PORT:-8000}" \
    --workers "${WEB_CONCURRENCY:-2}" \
    --timeout 120
