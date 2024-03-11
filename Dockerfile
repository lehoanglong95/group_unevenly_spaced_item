# Use Python 3.8 base image
FROM python:3.8

# Set working directory inside the container
WORKDIR /app

# Copy the contents of the local directory to the container's working directory
COPY . /app

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 3000
EXPOSE 3000

# Run the Python application
CMD ["python", "main.py"]
