FROM python:3.11-slim

# Env vars
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /srv
COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

# RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "-c", "./backend/gunicorn.py", "backend.wsgi"]
