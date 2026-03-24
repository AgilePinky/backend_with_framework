from pydantic import BaseModel, ConfigDict, Field

from utils.constants import MIN_GRADE, MAX_GRADE


class GradeStatisticResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=MIN_GRADE, description=">=0")
    min: int | None = Field(ge=MIN_GRADE, le=MAX_GRADE, description="[0, 5]")
    max: int | None = Field(ge=MIN_GRADE, le=MAX_GRADE, description="[0, 5]")
    avg: float | None = Field(ge=MIN_GRADE, le=MAX_GRADE, description="[0, 5]")
