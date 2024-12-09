import click
from flask.cli import with_appcontext
from db.utils.user import create_user
from webapp.app import app


@app.cli.command("create-admin")
@click.argument("username", required=True)
@click.argument("comisson", required=True)
@click.argument("webhook_url", required=True)
@with_appcontext
def create_admin_cli(username: str,
                     comisson: float,
                     webhook_url: str):
    create_user(username, comisson, webhook_url)
    print(f"Admin {username} created")
