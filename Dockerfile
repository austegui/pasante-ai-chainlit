FROM python:3.11-slim
WORKDIR /app

# -------- deps --------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------- code --------
COPY . .

EXPOSE 8080

# -------- run --------
CMD sh -c 'chainlit run app.py \
           --host 0.0.0.0 \
           --port ${PORT:-8080} \
           --headless \
           --config-file /app/config/chainlit.toml'
