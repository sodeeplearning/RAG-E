FROM ubuntu:latest

RUN apt update
RUN apt -y install curl

RUN curl https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb > cuda-keyring.deb
RUN dpkg -i cuda-keyring.deb
RUN apt update
RUN apt -y install cuda-toolkit-12-6
RUN rm cuda-keyring.deb

RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ["ollama", "serve"]
RUN ["ollama", "pull", "owl/t-lite:latest"]

RUN apt install python3.12

RUN pip install -r api/requirements.txt
RUN pip install -r rage/requirements.txt
RUN pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121

WORKDIR /app

COPY ./api ./api
COPY ./rage ./rage
