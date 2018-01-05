from flask import *


views = Blueprint('views', __name__)


@views.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@views.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@views.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
