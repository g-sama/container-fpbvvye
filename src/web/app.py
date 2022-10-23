from datetime import date
from math import floor
from time import time
from flask import Flask, redirect, render_template, request, url_for
# from db import get_db, close_db
# import sqlalchemy
# from logger import log
from deta import Deta

# initialize with a project key
deta = Deta("d0qprvt5_hbyBNnNXABFzmPQq3e8vhBhmXde8w42k")

# create and use as many Drives as you want!
drive = deta.Drive("first_micro")

app = Flask(__name__)
# app.teardown_appcontext(close_db)


@app.route("/files")
def test():
    item_list = drive.list()
    return item_list

@app.route('/api/v1/save-assests', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        file = request.files["assest"]
        res = drive.put(f'{floor(time()*10000)}-{file.filename}', file)
        print(res)
        return res
    else:
        return render_template("error.html")

@app.route("/api/v1/assests-list")
def item_list():
    item_list = drive.list()
    return item_list

@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/health")
# def health():
#     log.info("Checking /health")
#     db = get_db()
#     health = "BAD"
#     try:
#         result = db.execute("SELECT NOW()")
#         result = result.one()
#         health = "OK"
#         log.info(f"/health reported OK including database connection: {result}")
#     except sqlalchemy.exc.OperationalError as e:
#         msg = f"sqlalchemy.exc.OperationalError: {e}"
#         log.error(msg)
#     except Exception as e:
#         msg = f"Error performing healthcheck: {e}"
#         log.error(msg)

#     return health


if __name__ == '__main__':
   app.run(debug=True)