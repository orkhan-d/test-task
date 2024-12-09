from db.base import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime as dt


class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    balance: Mapped[float] = mapped_column(server_default='0')
    commission: Mapped[float] = mapped_column()
    webhook_url: Mapped[str] = mapped_column()

    created_at: Mapped[dt] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt] = mapped_column(server_default=func.now(),
                                           server_onupdate=func.now())