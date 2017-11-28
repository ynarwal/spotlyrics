FROM python:3.6
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
COPY ./ /code
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN useradd -m django
USER django
ENV PORT 8000
EXPOSE 8000
CMD gunicorn \
  --bind 0.0.0.0:$PORT \
  --timeout 15 \
  --workers 4 \
  spotifyapi.wsgi
