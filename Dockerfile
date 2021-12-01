FROM python:3.10

COPY . /app
WORKDIR /app

EXPOSE 5005

RUN pip install -r requirements.txt

# ENTRYPOINT exec uvicorn main:app --port 5001 --server-header --log-level debug --app-dir src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5005", "--app-dir", "src"]
