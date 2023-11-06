FROM python:3.7

WORKDIR /app

COPY . /app/

RUN pip install flask

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]