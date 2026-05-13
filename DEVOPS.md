# DevOps Setup

This project includes Docker containerization and a GitHub Actions workflow for the Django freelancing platform.

## Docker

Build the image:

```bash
docker build -t django-freelancing-platform .
```

Run the container:

```bash
docker run -p 8000:8000 \
  -e SECRET_KEY=change-this-secret-key \
  -e DEBUG=0 \
  -e ALLOWED_HOSTS=127.0.0.1,localhost \
  django-freelancing-platform
```

For local Docker Compose usage:

```bash
docker compose up --build
```

Then open:

```text
http://localhost:8000
```

## GitHub Actions

The workflow is stored at:

```text
.github/workflows/django-ci.yml
```

On every push or pull request to `main` or `master`, it:

1. Installs Python dependencies.
2. Runs `python manage.py check`.
3. Runs `python manage.py test`.
4. Builds the Docker image.

## Deployment Environment Variables

Use these variables on a production server or cloud platform:

```text
SECRET_KEY=your-production-secret-key
DEBUG=0
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://user:password@host:5432/dbname
```

If `DATABASE_URL` is not set, the app uses the local SQLite database.
