from pydantic import Field

GRADE_VALUES = Field(ge=0, le=5, description="[0, 5]")
COUNT_VALUE = Field(ge=0, description=">=0")
MIN_GRADE: int = 0
MAX_GRADE: int = 0
