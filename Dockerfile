# Using official Python image
FROM python:3.9-slim

# Setting working directory in the container
WORKDIR /app

# Copy local files to the container
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Exposing port Flask will run on
EXPOSE 5000


CMD ["python", "app.py"]
