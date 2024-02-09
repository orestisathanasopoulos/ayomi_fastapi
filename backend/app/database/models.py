from typing import Optional
from sqlalchemy import Identity, MetaData, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime


class Base(DeclarativeBase):
    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True)
    }


class OperationWithResult(Base):
    __tablename__ = "operations"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    operation: Mapped[str] = mapped_column(index=True)
    result: Mapped[float]
    time_created: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now())
    time_updated: Mapped[Optional[datetime.datetime]
                         ] = mapped_column(onupdate=func.now())


metadata = MetaData()
