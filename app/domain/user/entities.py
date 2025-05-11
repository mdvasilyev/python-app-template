from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
