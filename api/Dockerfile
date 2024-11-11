FROM ubuntu:latest

RUN apt update
RUN apt -y install curl

RUN curl https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb > cuda-keyring.deb
RUN dpkg -i cuda-keyring.deb
RUN apt update
RUN apt -y install cuda-toolkit-12-6
RUN rm cuda-keyring.deb


FROM ollama/ollama

CMD ollama run owl/t-lite:latest


FROM python:3.12-slim

WORKDIR /app

COPY ./api ./api
COPY ./rage ./rage

RUN pip3 install -r api/requirements.txt
RUN pip3 install -r rage/requirements.txt
RUN pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121

CMD ["python", "api/main.py"]
