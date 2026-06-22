FROM python:3.9-slim
WORKDIR /app
COPY . .
# Standart qiymatlar
ENV APP_MODE=production
ENV DB_HOST=db.example.com
CMD ["python", "main.py"]
