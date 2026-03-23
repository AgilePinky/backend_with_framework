from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class GradeStatisticResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0, description=">=0")
    min: Optional[int] = Field(ge=0, le=5, description="[0, 5]")
    max: Optional[int] = Field(ge=0, le=5, description="[0, 5]")
    avg: Optional[float] = Field(ge=0, le=5, description="[0, 5]")
