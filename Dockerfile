FROM docker.io/library/python:3.8-alpine
WORKDIR /app
EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=0

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./app .
CMD ["flask", "run"]