FROM python:3

# Install the required libraries
RUN pip install kubernetes

# Copy the webhook code to the image
# COPY webhook.py /app/webhook.py
COPY data.json /app/data.json
COPY readAndTrigger.py /app/webhook.py

# Run the webhook when the container starts
CMD ["python", "-u", "/app/webhook.py"]
