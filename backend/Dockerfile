# Development stage
FROM python:3.9-slim as development

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_ENV=development

# Set the working directory in the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

RUN chmod +x entrypoint.sh

# Expose the port on which the Flask app will run
EXPOSE 5000

# Development entrypoint
ENTRYPOINT ["./entrypoint.sh"]

# Production stage
FROM python:3.9-slim as production

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_ENV=production

# Set the working directory in the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

RUN chmod +x entrypoint.sh

# Expose the port on which the Flask app will run
EXPOSE 5000

# Production entrypoint
ENTRYPOINT ["./entrypoint.sh"]
