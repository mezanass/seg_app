# Use an official Python runtime as a parent image
FROM tensorflow/tensorflow:1.12.0-py3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
# ENV NAME World
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Run app.py when the container launches
CMD ["python", "seg_app.py"]

