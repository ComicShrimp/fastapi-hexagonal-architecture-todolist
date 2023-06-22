from fastapi import APIRouter

from ..responses import Success

router = APIRouter()


@router.get("/", response_model=Success)
async def root() -> Success:
    return Success(message="OK")
