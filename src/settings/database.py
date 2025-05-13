from datetime import datetime
from typing import Annotated

from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declared_attr, Mapped, mapped_column

from settings.constants import DB_URL


engine = create_engine(DB_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)

int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[
    datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)
]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int_pk]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
