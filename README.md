# RAG-E
**Retrieval Augmented Generations** for **Everyone**.

AI framework made for simply-working with [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) pipelines.

![RAG architecture](https://blogs.nvidia.com/wp-content/uploads/2023/11/Retrieval-Augmented-Generation-RAG-KV-1.jpg)

### Start using RAG-E tutorial
Install repo to your project directory via git clone:
```bash
git clone https://github.com/sodeeplearning/RAG-E
```
Start using RAG in Python:
```python
from rage.rag import RAG

assistant = RAG(["file1.pdf", "file2.docx", "file3.txt"])
print(assistant("What was in these documents?"))
```


## API
Read [API Documentation](https://github.com/sodeeplearning/RAG-E/blob/main/api/README.md) to get more information.

### Start API locally
Before starting API download and launch Ollama from [Official Source](https://ollama.com/download)


Starting API via uvicorn:
```bash
git clone https://github.com/sodeeplearning/RAG-E
cd RAG-E
pip install -r api/requirements.txt
pip install -r rage/requirements.txt
ollama pull owl/t-lite:latest
uvicorn api/main:api
```

### Start API with Docker
To build Dockerfile in /api folder:
```bash
git clone https://github.com/sodeeplearning/RAG-E
cd RAG-E
docker build . -f api/Dockerfile -t rage-api
docker run -it --gpus=all rage-api  
```

## For partnership
If you are interested in this project, but you need to get personal offer:

**Be brave** to text the team: ```vitaliy.petreev@gmail.com```

## For contributors 💘
1) Create fork from ```main``` branch
2) Make your changes
3) Create pull request from your fork to ```dev``` branch with description of implemented changes
4) Wait for approving
5) **You're officially part of the project!**

## Team info
[Vitaliy Petreev](https://github.com/sodeeplearning) - HEAD of the project.
