from flask import *
from . import views


app = Flask(__name__)

app.register_blueprint(views.views)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
