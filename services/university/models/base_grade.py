from pydantic import BaseModel, ConfigDict, Field

from services.university.models.constants import MIN_GRADE, MAX_GRADE


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: int = Field(ge=MIN_GRADE, le=MAX_GRADE,
                       description=f"[{MIN_GRADE}, {MAX_GRADE}]")
