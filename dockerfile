# Dockerfile
FROM tuankhanhtran520/noventiq:base

WORKDIR /app

# Copy app files
COPY ./App/ .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by your app
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
