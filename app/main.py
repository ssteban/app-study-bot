from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(user.router, prefix="/user", tags=["user"])



