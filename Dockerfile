FROM python:3.6.4-stretch

ENV TZ Asia/Kolkata
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["gunicorn","-b","0.0.0.0:8107","--access-logfile","-","app:app", "--reload"]