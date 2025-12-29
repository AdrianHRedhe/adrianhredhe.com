from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Input(BaseModel):
    name: str


class Output(BaseModel):
    greeting: str


@router.post("/api", response_model=Output)
def predict(payload: Input):
    """
    Toy API just to ensure posts work as they should.
    """
    greeting = f"Hello {payload.name}"
    return {"greeting": greeting}
