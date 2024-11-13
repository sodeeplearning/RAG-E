# RAG-E
**Retrieval Augmented Generations** for **Everyone**.

AI framework made for simply-working with [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) pipelines.

### Start using RAG-E tutorial
Install repo to your project directory via git clone:
```bash
git clone https://github.com/sodeeplearning/RAG-E
```
Start using RAG in Python:
```python
from rage.rag import RAG

assistant = RAG(["file1.pdf", "file2.docs", "file3.txt"])
print(assistant("What was in these documents?"))
```


## API
Read [API Documentation](https://github.com/sodeeplearning/RAG-E/blob/main/api/README.md) to get more information.
### Start API locally
Starting API via uvicorn:
```bash
git clone https://github.com/sodeeplearning/RAG-E
cd RAG-E
pip install -r api/requirements.txt
pip install -r rage/requirements.txt
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

### Team info
[Vitaliy Petreev](https://github.com/sodeeplearning) - HEAD of the project.
