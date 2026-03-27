from pydantic import BaseModel, ConfigDict, Field

from services.university.models.constants import MIN_GRADE, MAX_GRADE


class GradeStatisticResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0, description=">=0")
    min: int | None = Field(ge=MIN_GRADE, le=MAX_GRADE,
                       description=f"[{MIN_GRADE}, {MAX_GRADE}]")
    max: int | None = Field(ge=MIN_GRADE, le=MAX_GRADE,
                       description=f"[{MIN_GRADE}, {MAX_GRADE}]")
    avg: float | None = Field(ge=MIN_GRADE, le=MAX_GRADE,
                       description=f"[{MIN_GRADE}, {MAX_GRADE}]")
