from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, 

from settings.database import Base, str_uniq


class User(Base):
    uuid: Mapped[str_uniq]
    territory_account: Mapped[int] = mapped_column(server_default=text("0"))

    territorys: Mapped[list["Territory"]] = relationship("Territory", back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "uuid": self.uuid,
            "territory_account": self.territory_account,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        
class Territory(Base):
    x1: Mapped[int]
    y1: Mapped[int]
    x2: Mapped[int]
    y2: Mapped[int]
    area: Mapped[int]
    user_uuid: Mapped[str] = mapped_column(ForeignKey("users.uuid"))

    user: Mapped["User"] = relationship("User", back_populates="territorys")

    def to_dict(self):
        return {
            "id": self.id,
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "area": self.area,
            "user_uuid": self.user_uuid,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    