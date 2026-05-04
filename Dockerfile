# 1. Start with a Python base image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your project files into the container
COPY . .

# 4. Install your Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Tell the container how to run your app
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]