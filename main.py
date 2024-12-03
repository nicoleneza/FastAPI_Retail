from fastapi import FastAPI
from app.accounts.routers import router as accounts_router
from app.inventory.routers import router as inventory_router
from database import Base,engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(accounts_router,prefix='/accounts',tags=['accounts'])
app.include_router(inventory_router,prefix='/products',tags=['products'])

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

