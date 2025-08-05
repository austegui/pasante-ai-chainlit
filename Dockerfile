FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8080
CMD sh -c 'chainlit run \
           --config-file /app/config/chainlit.toml \
           --host 0.0.0.0 \
           --port ${PORT:-8080} \
           --headless \
           app.py'

