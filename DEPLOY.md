# Deploying this project on Render

This repo is ready for a one-click [Render Blueprint](https://render.com/docs/infrastructure-as-code) deploy.
`render.yaml` creates a Python web service plus a managed PostgreSQL database.

## What's already configured

| File | Purpose |
| --- | --- |
| `render.yaml` | Web service + Postgres, env vars, build/start commands |
| `build.sh` | Installs deps, `collectstatic`, `migrate`, seeds demo catalogue |
| `.python-version` | Pins Python 3.14 |
| `ecommerce/settings.py` | Reads `DEBUG`, `SECRET_KEY`, `DATABASE_URL`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` from the environment; WhiteNoise for static files |
| `core/fixtures/catalog.json` | 14 demo products, 10 categories, specs and trending rows |
| `core/management/commands/seed_catalog.py` | Loads the fixture only when the database is empty |

## Deploy steps

1. Push this repo to GitHub (already wired: `rahulrameshm0/Shopify`).
2. Open <https://dashboard.render.com/blueprints> → **New Blueprint Instance**.
3. Select the **Shopify** repo and click **Connect**.
4. Give the blueprint a name, then **Apply**.
5. Wait for the first build (~3-5 min). The app is live at `https://<service-name>.onrender.com`.

Render generates `SECRET_KEY` automatically and injects `DATABASE_URL`,
`RENDER_EXTERNAL_HOSTNAME` and `RENDER_EXTERNAL_URL`.

## After the first deploy

Set the optional secrets in the dashboard (**Environment** tab):

- `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET` — checkout will 500 without them
- `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` — for account emails

Create an admin user from the Render **Shell**:

```bash
python manage.py createsuperuser
```

Then log in at `/admin/`.

## Things to know about the free plan

- **Cold starts:** free web services sleep after ~15 minutes of inactivity.
- **Ephemeral disk:** uploaded images (new products, profile pictures) are lost on
  restart/deploy. The 14 demo products ship with the repo, so they survive.
  To persist uploads, add a disk (uncomment the `disk:` block in `render.yaml`)
  and set `MEDIA_ROOT=/var/data/media`.
- **Free Postgres expires** about 30 days after creation; upgrade the database
  plan to keep data long-term.

## Custom domain

Add the domain in Render, then append it to the env vars:

```
DJANGO_ALLOWED_HOSTS = .onrender.com,yourdomain.com
CSRF_TRUSTED_ORIGINS = https://*.onrender.com,https://yourdomain.com
```

## Local development

The existing Docker setup still works (`docker compose up`) and reads `.env`.
Alternatively, without Docker:

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_catalog   # optional demo data
python manage.py runserver
```
