from pydantic import BaseModel, Field


class SignedMS(BaseModel):
    message: str = Field(..., pattern=r"^te_\w+$")
    signature: str = Field(...)
