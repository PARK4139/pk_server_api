FROM python:3.11-slim

WORKDIR /web
COPY ./app /web/app
COPY requirements.txt /web/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
