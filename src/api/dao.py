from settings.base import BaseDAO

from api.model import User


class UserDAO(BaseDAO):
    model = User