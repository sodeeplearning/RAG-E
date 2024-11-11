from fastapi import FastAPI
import uvicorn
import handlers


api = FastAPI()
api.include_router(handlers.router)


if __name__ == '__main__':
    uvicorn.run(api)
