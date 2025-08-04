FROM python:3.11-slim

WORKDIR /app

#  -- dependencias --
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#  -- código fuente (ya sin .chainlit) --
COPY . .

EXPOSE 8080

#   ① elimina posibles restos de config
#   ② usa el puerto que inyecta DigitalOcean ($PORT)
#   ③ headless para que no abra el navegador
CMD ["sh", "-c", "rm -f /app/.chainlit/config.toml && exec chainlit run app.py --host 0.0.0.0 --port ${PORT:-8080} --headless"]

