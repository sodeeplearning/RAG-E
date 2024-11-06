from fastapi import FastAPI

import handlers

api = FastAPI()
api.include_router(handlers.router)

@api.on_event("startup")
async def startup_event():
    pass
