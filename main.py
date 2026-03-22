from fastapi import FastAPI
from cadastro import router as cadastro_router
from login import router as login_router

app = FastAPI()

app.include_router(cadastro_router)
app.include_router(login_router)
