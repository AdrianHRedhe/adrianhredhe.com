from fastapi import APIRouter

from app.models.dataclasses import ApiInput, ApiOutput

router = APIRouter()


@router.post("/api", response_model=ApiOutput)
def predict(payload: ApiInput):
    """
    Toy API just to ensure posts work as they should.
    """
    greeting = f"Hello {payload.name}"
    return {"greeting": greeting}
