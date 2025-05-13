from pydantic import BaseModel

from settings.constants import MAX_TERRITORY


class User(BaseModel):
    uuid: str
    terr_limit: int = MAX_TERRITORY
    terrs: list[str] = []
    
class RBParams:
    def __init__(self):
        pass
    
    def to_dict(self):
        pass