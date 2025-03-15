FROM python:3.9-slim

WORKDIR /app

# کپی کردن فایل requirements.txt به داخل کانتینر
COPY requirements.txt /app/

# نصب کتابخانه‌ها از فایل requirements.txt
RUN pip install -r requirements.txt

# کپی کردن باقی‌مانده فایل‌ها به داخل کانتینر
COPY . .

# اجرای اپلیکیشن FastAPI با Uvicorn
CMD ["uvicorn", "code_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
