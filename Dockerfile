# ---------- base image ----------
FROM python:3.11-slim

# ---------- working dir ----------
WORKDIR /app

# ---------- Python deps ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- source code ----------
COPY . .

# ---------- runtime ----------
EXPOSE 8080
CMD ["chainlit", "run", "app.py",
     "--host", "0.0.0.0",
     "--port", "${PORT:-8080}",
     "--headless",
     "-c", "/app/config/chainlit.toml"]
