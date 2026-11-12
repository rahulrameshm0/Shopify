#!/usr/bin/env bash
# Build script used by Render on every deploy.
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# Collect CSS/JS/images for WhiteNoise to serve.
python manage.py collectstatic --noinput

# Create/update the database schema.
python manage.py migrate --noinput

# Populate the store with the bundled catalogue on first deploy only.
python manage.py seed_catalog
