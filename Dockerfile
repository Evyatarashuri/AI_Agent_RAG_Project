# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for PyPDF2 or other requirements)
RUN apt-get update && apt-get install -y gcc libffi-dev libxml2-dev libxslt1-dev libjpeg-dev zlib1g-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app ./app
COPY static ./static

# Set environment variables
ENV FLASK_APP=app.main
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Expose port
EXPOSE 8000

# Start the app
CMD ["flask", "run"]
