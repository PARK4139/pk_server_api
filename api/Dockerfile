FROM python:3.11-slim

WORKDIR /api
COPY ./app /api/app
COPY requirements.txt /api/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
