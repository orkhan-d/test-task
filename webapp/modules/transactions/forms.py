from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField
from wtforms.validators import DataRequired


class TransactionCreateForm(FlaskForm):
    id = IntegerField("id", validators=[])
    amount = FloatField("amount", validators=[DataRequired()])
    user_id = IntegerField("user_id", validators=[DataRequired()])
