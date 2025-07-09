FROM python:3-slim
WORKDIR /usr/src/app
COPY src/* ./
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt
RUN apt update
RUN apt upgrade -y
RUN apt install -y git

ENTRYPOINT ["python", "/usr/src/app/main.py"]