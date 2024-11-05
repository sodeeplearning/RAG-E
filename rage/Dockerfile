FROM ollama/ollama
FROM python:3.12-slim-bullseye

WORKDIR /rage


COPY ../requirements.txt rag_requirements.txt

CMD ["ollama", "pull", "owl/t-lite:latest"]
RUN pip install -r rag_requirements.txt


COPY .. .
