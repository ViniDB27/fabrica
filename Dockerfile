FROM python:3.9

WORKDIR /app

RUN pip install django

COPY requirements.txt .

RUN python -m pip install --upgrade pip

# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=postgres \
    POSTGRES_HOST=db \
    POSTGRES_PORT=5432 \
    POSTGRES_DB=mydatabase

RUN python manage.py migrateclear

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
