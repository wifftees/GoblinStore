from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from configparser import ConfigParser
from database import StoreConnection, Users
from utils import send_messages
from urllib import parse
import asyncio

app = Flask(__name__)
Bootstrap(app)

config = ConfigParser()
config.read("config.ini")

token = config["TELEGRAM"]["token"]

connection = StoreConnection.get_connection(
    config["DATABASE"]["username"],
    config["DATABASE"]["password"]
)

database = connection[config["DATABASE"]["name"]]
users = Users(database)


@app.route("/", methods=["GET", "POST"])
def admin_page():
    if request.method == "POST":
        form = request.form
        message = form.get("users-message-area")
        premium = True if form.get("premium") == "" else False
        default = True if form.get("default") == "" else False
        if default and premium:
            all_users = users.get_all_users()
            all_users_chat_id = [user["chat_id"] for user in all_users]
            asyncio.run(send_messages(all_users_chat_id, parse.quote(message)))
        elif premium:
            premium_users = users.get_premium_users()
            premium_users_chat_id = [user["chat_id"] for user in premium_users]
            asyncio.run(send_messages(premium_users_chat_id, parse.quote(message)))
        elif default:
            default_users = users.get_default_users()
            default_users_chat_id = [user["chat_id"] for user in default_users]
            asyncio.run(send_messages(default_users_chat_id, parse.quote(message)))
        return redirect(url_for('admin_page'))

    all_users = users.get_all_users()
    return render_template("index.html", users=all_users)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
