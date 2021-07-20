from flask import Flask
from init_db import *
from view import *

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
