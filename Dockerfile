# Use official Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]