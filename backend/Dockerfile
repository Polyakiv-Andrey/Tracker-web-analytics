FROM python:3.10-slim

EXPOSE 8000

WORKDIR /django

COPY requirements.txt /django
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /django

CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]

