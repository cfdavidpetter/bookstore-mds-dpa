# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code to the working directory
COPY . .

RUN chmod +x entrypoint.sh

# Expose the port on which the Flask app will run (adjust if necessary)
EXPOSE 5000

# ...

# Run the Flask development server
ENTRYPOINT ["./entrypoint.sh"]
