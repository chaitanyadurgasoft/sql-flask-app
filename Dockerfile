FROM python:3.9-slim

WORKDIR /app
RUN pip install --upgrade pip
# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the container port
EXPOSE 5000

# Set the entry point of the container
CMD flask run -h 0.0.0.0 -p 5000
