from flask import Blueprint, request
from webapp.modules.transactions.forms import TransactionCreateForm

blueprint = Blueprint("transactions", __name__)


@blueprint.route("/create_transactions",
                 methods=["POST"])
def create_transaction():
    if request.method == "POST":
        form = TransactionCreateForm()
        if form.validate_on_submit():
            return form.data
        else:
            return form.errors
    else:
        return "some form"