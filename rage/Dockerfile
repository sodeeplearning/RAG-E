FROM ollama/ollama

WORKDIR /rage


COPY ../requirements.txt rag_requirements.txt

RUN ["ollama", "pull", "owl/t-lite:latest"]
RUN pip install -r rag_requirements.txt


COPY . .
