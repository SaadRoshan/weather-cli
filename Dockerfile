# Start from an official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies file first
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the code
ENV OPENWEATHER_API_KEY=""

# Copy the rest of the code
COPY src/ ./src/

# Run the app
CMD ["python", "src/main.py"]