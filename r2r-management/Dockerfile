FROM python:3.12-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
RUN chmod +x entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
