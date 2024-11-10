import subprocess

from fastapi import FastAPI
import uvicorn

subprocess.run(["ollama", "serve"])
subprocess.run(["ollama", "pull", "owl/t-lite:latest"])

import handlers


api = FastAPI()
api.include_router(handlers.router)


if __name__ == '__main__':
    uvicorn.run(api)
