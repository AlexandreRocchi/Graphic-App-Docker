FROM python:3.9-slim


RUN apt-get update && \
    apt-get install -y python3-tk


RUN pip install customtkinter


COPY app.py /app/app.py


WORKDIR /app


CMD ["python", "app.py"]
