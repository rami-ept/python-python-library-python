from flask import Flask, render_template
import importlib

fakepypiproject = importlib.import_module("fake-pypi-project")

from fakepypiproject.core import get_message


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html',
        message=get_message())


def run_server():
    app.run()