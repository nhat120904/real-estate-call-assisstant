# Use an official Python runtime as the base image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code into the container
COPY . .

# Expose the port your Python application will run on (if applicable)
EXPOSE 8765
EXPOSE 8766

# Command to run your Python application
CMD ["python", "demo3.py"]
