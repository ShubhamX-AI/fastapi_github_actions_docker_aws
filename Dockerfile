FROM python:3.10-slim

WORKDIR /app

# Add this line to accept the TAG build argument
ARG TAG 

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]