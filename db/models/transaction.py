from sqlalchemy import ForeignKey

from db.base import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from enum import Enum

from datetime import datetime as dt

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

    created_at: Mapped[dt] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt] = mapped_column(server_default=func.now(),
                                           server_onupdate=func.now())