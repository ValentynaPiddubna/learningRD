
FROM python:3.11.0

WORKDIR /data

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install celery


COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
