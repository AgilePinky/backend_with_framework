from pydantic import BaseModel, ConfigDict
from typing_extensions import Literal


class LoginResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    access_token: str
    token_type: Literal["Bearer"]