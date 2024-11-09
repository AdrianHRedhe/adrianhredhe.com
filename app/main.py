# %%
from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import render_markdown

app = FastAPI()


class Input(BaseModel):
    name: str

class Output(BaseModel):
    greeting: str


@app.get("/")
def home():
    return {"health_check": "OK"}

@app.get("/readme")
def readme():
    return render_markdown("README.md", {"Creator": "Adde"})


@app.post("/api", response_model=Output)
def predict(payload: Input):
    greeting = f"Hello {payload.name}"
    return {"greeting": greeting}
