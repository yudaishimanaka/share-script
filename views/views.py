from flask import *


views = Blueprint('views', __name__)


@views.route('/register', methods=['GET'])
def register():
    return render_template('register.html')
