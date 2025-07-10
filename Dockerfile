FROM python:3-slim
WORKDIR /usr/src/app
COPY src/* ./
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt
RUN apt update
RUN apt upgrade -y
RUN apt install -y git
RUN git config --global --add safe.directory /github/workspace

ENTRYPOINT ["python", "/usr/src/app/main.py"]