from typing import Literal

from pydantic import BaseModel


class Ok(BaseModel):
    """OK response."""

    status: Literal["ok"] = "ok"
