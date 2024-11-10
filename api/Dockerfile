FROM ubuntu:latest

RUN apt update
RUN apt -y install curl

RUN curl https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb > cuda-keyring.deb
RUN dpkg -i cuda-keyring.deb
RUN apt update
RUN apt -y install cuda-toolkit-12-6
RUN rm cuda-keyring.deb

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.12 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./api ./api
COPY ./rage ./rage

RUN pip3 install -r api/requirements.txt
RUN pip3 install -r rage/requirements.txt
RUN pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121


WORKDIR /app/api

CMD ["python", "-m", "main.py"]
