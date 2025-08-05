FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# —— limpia capas anteriores del builder/cache ——
RUN rm -rf /app/.chainlit

COPY . .

EXPOSE 8080
CMD ["chainlit", "run", "app.py",
     "--host", "0.0.0.0",
     "--port", "8080",
     "--headless",
     "-c", "/app/config/chainlit.toml"]

