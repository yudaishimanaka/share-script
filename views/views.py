from flask import *
from database import Session as Ss
from models import User


views = Blueprint('views', __name__)


@views.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@views.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@views.route('/index', methods=['GET'])
def index():
    if session:
        user = Ss.query(User).filter_by(user_id=session['user_id']).one()
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')


@views.route('/setting', methods=['GET'])
def setting():
    if session:
        user = Ss.query(User).filter_by(user_id=session['user_id']).one()
        return render_template('setting.html', user=user)
    else:
        return render_template('setting.html')
