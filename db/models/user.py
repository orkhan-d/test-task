from db.base import db
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    balance: Mapped[float] = mapped_column(server_default='0')
    commission: Mapped[float] = mapped_column()
    webhook_url: Mapped[str] = mapped_column()
