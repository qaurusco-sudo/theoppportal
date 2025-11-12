from fastapi import FastAPI
from app.routers import auth

app = FastAPI()

# 👇 important: prefix must match the route we’re testing
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "The Opp Portal API is running 🚀"}