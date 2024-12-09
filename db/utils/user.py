from db.models.user import User
from db.base import db


def create_user(name: str,
                commission: str,
                webhook_url: str,
                balance: float = 0.0):
    user = User(name=name,
                commission=commission,
                webhook_url=webhook_url,
                balance=balance)
    db.session.add(user)
    db.session.commit()

    return user
