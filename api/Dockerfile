# Start from an official Python 3.11 image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt requirements.txt

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the other code into the container
COPY . .

# This is the command that will run when the container starts.
# It tells 'uvicorn' to run the 'app' object from the 'main.py' file.
# 'host 0.0.0.0' makes it accessible from outside the container.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]