# 1. Start with Python 3.11
FROM python:3.11-slim

# 2. Install system dependencies needed for OSINT/Image tools
# We add build-essential for compiling and libgl1 for image processing
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory
WORKDIR /app

# 4. Copy everything
COPY . .

# 5. Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# 6. Launch the Streamlit UI
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]