from sqlalchemy import ForeignKey

from db.base import db
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum


class TransactionStatus(Enum):
    PENDING = 'ожидание'
    CONFIRMED = 'подтвеждена'
    CANCELED = 'отменена'
    EXPIRED = 'истекла'


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id',
                                                    ondelete='CASCADE',
                                                    onupdate='CASCADE'))
    amount: Mapped[float] = mapped_column()
    commission: Mapped[float] = mapped_column()
    status: Mapped[TransactionStatus] = mapped_column(db.Enum)
