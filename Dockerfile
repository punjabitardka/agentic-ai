# 1. Start with Python 3.11 (or higher) to satisfy requirements
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy everything
COPY . .

# 4. Install libraries (this should work now!)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Launch the Streamlit UI
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]