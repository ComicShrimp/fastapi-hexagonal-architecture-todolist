from uuid import UUID

from pydantic import BaseModel


class Created(BaseModel):
    id: UUID
