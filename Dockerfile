# Start with a small, official Python environment
FROM python:3.11-slim

# Create a folder inside the container for our app
WORKDIR /app

# Copy the requirements file first to install libraries
COPY requirements.txt .

# Install the libraries (requests and pytest)
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else from your project into the container
COPY . .

# Tell the container to run your script when it starts
CMD ["python", "downloader.py"]