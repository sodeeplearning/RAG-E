FROM ubuntu:latest

RUN apt update
RUN apt -y install curl

RUN curl https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb > cuda-keyring.deb
RUN dpkg -i cuda-keyring.deb
RUN apt update
RUN apt -y install cuda-toolkit-12-6
RUN rm cuda-keyring.deb


FROM ollama/ollama

RUN ollama pull owl/t-lite:latest


FROM python:3.12-slim

WORKDIR /app

COPY ./api/rage/requirements.txt rage-reqs.txt
COPY ./api/requirements.txt api-reqs.txt

RUN pip3 install -r api-reqs.txt
RUN pip3 install -r rage-reqs.txt
RUN pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121

COPY ./api ./api

CMD ["fastapi", "run", "api/main.py", "--port", "80"]
#CMD ["python3.12", "api/main.py"]
