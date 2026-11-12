# Shopify — Django E-Commerce Store

A full-stack e-commerce web application built with Django: product catalogue,
search, cart, wishlist, reviews, user accounts, and Razorpay checkout.

**Live demo:** https://shopify-b5g9.onrender.com
**Admin:** https://shopify-b5g9.onrender.com/admin/

> The demo runs on Render's free tier, so the first request after ~15 minutes of
> inactivity can take 30–60 seconds while the instance wakes up.

---

## Features

- **Catalogue** — categories, product listing, product detail pages with
  specifications, and a "trending" section driven by `TrendingProduct`
- **Search** — keyword search across products
- **Accounts** — register, sign in/out, profile page with avatar upload,
  edit profile, and password reset by email
- **Cart** — add/remove items, increase/decrease quantity, live cart count in
  the navbar via a context processor
- **Wishlist** — add/remove/clear, with a badge count in the navbar
- **Reviews** — per-product ratings and comments
- **Checkout** — order + order items created in the database, Razorpay payment
  order created server-side, signature verification on callback
- **Admin** — full Django admin for products, categories, orders, reviews and
  users
- **Production ready** — WhiteNoise static serving, env-driven settings,
  Gunicorn, PostgreSQL or SQLite support

## Tech stack

| Layer | Technology |
| --- | --- |
| Backend | Django 6.0, Python 3.14 |
| Database | PostgreSQL (production-ready) / SQLite (current demo) |
| Payments | Razorpay |
| Static files | WhiteNoise |
| Server | Gunicorn |
| Frontend | Django templates, HTML, CSS, JavaScript |
| Deployment | Render (`render.yaml`, `build.sh`, `start.sh`) |

## Project structure

```
.
├── accounts/        # auth, profiles, password reset
├── cart/            # cart models, views, context processor
├── categories/      # product categories
├── core/            # shared utilities, seed + superuser commands, fixtures
├── dashboard/       # dashboard app
├── ecommerce/       # settings, urls, wsgi/asgi
├── home/            # landing page, static informational pages
├── orders/          # checkout, orders, Razorpay integration
├── payments/        # payments app
├── products/        # products, specifications, trending products
├── reviews/         # product reviews
├── search/          # product search
├── wishlist/        # wishlist models, views, context processor
├── static/          # CSS, JS, images
├── templates/       # HTML templates
├── media/           # uploaded + demo product images
├── build.sh         # Render build step
├── start.sh         # Render start step (migrate, seed, Gunicorn)
├── render.yaml      # Render blueprint
└── DEPLOY.md        # deployment notes
```

## Running locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` in the project root:

```env
SECRET_KEY=change-me
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL)
DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Optional
RAZORPAY_KEY_ID=
RAZORPAY_KEY_SECRET=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Then:

```bash
python manage.py migrate
python manage.py seed_catalog        # optional demo catalogue
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000.

### With Docker

```bash
docker compose up --build
```

This starts the web service and a PostgreSQL 17 container using `.env`.

### With SQLite (no Postgres needed)

```bash
export DATABASE_URL="sqlite:///$(pwd)/db.sqlite3"
python manage.py migrate
python manage.py runserver
```

## Configuration

Settings are read from the environment (via `python-decouple` / `os.environ`):

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Django secret (required when `DEBUG=False`) |
| `DEBUG` | `True` / `False` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hostnames |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated trusted origins (https://…) |
| `DATABASE_URL` | Full database URL; overrides the `DB_*` variables |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | Postgres connection |
| `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET` | Razorpay credentials |
| `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` | SMTP account for password reset |
| `MEDIA_ROOT` | Override media directory (e.g. a mounted disk) |
| `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` | Optional boot-time admin creation |

Render injects `RENDER_EXTERNAL_HOSTNAME` and `RENDER_EXTERNAL_URL`, which are
added to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` automatically.

## Management commands

```bash
python manage.py seed_catalog        # load demo products if the catalogue is empty
python manage.py ensure_superuser    # create admin from DJANGO_SUPERUSER_* env vars
```

## Deployment

See [DEPLOY.md](DEPLOY.md) for the full Render setup, environment variables and
caveats (free-tier sleeping, ephemeral SQLite, single free Postgres slot).

Push to `main` and Render redeploys automatically.

## License

Personal learning project — use it as you like.
