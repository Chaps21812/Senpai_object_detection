FROM python:3.12-alpine

WORKDIR /app
COPY requirements_conda.txt .
COPY requirements_pip.txt .
COPY ./YOLO_model /app/YOLO_model
RUN pip install --no-cache-dir -r requirements_pip.txt

EXPOSE 30501

RUN useraadd app
USER app

# Set the entry point
ENTRYPOINT ["python", "main.py"]