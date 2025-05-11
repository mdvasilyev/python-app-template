from .entities import User
from .interfaces import AbstractUserRepository


class GetUserById:
    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo

    def execute(self, user_id: int) -> User | None:
        return self.repo.get_by_id(user_id)
