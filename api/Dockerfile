FROM nvidia/cuda:12.6.2-cudnn-devel-ubuntu22.04

RUN apt-get update
RUN apt-get install -y sudo
RUN sudo apt-get install -y python3-docker
RUN sudo apt-get install -y python3-pip

RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app

COPY ./rage/requirements.txt rage-reqs.txt
COPY ./api/requirements.txt api-reqs.txt

RUN pip3 install -r api-reqs.txt
RUN pip3 install -r rage-reqs.txt
RUN pip3 install --upgrade torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121

COPY ./api ./api
COPY ./rage ./api/rage

VOLUME ./api /app/api

CMD ["fastapi", "run", "api/main.py", "--port", "80"]
