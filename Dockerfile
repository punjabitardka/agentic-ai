# 1. Use Python 3.12 - This matches your modern setup better
FROM python:3.12-slim

# 2. Install EVERYTHING needed for OSINT, Image processing, and Compiling
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgl1-mesa-glx \
    libglib2.0-0 \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory
WORKDIR /app

# 4. Copy your files
COPY . .

# 5. Upgrade pip and install your requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 6. Start the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]