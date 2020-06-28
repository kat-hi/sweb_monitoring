# server setup
FROM python:3.6

RUN mkdir /app

COPY requirements.txt /app

COPY ./ /monitoring/

WORKDIR /monitoring

RUN chmod +x requirements.txt

RUN pip install -r requirements.txt --no-cache-dir --compile

ENV FLASK_ENV=production
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]