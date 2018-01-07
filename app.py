from flask import *
from views import views
from database import Session as Ss
from models import *
from passlib.hash import pbkdf2_sha256
import re
import configparser


app = Flask(__name__)

app.register_blueprint(views.views)
config = configparser.ConfigParser()
config.read('app.conf')
app.secret_key = config['SECRET']['SECRET_KEY']


@app.route('/create_user', methods=['POST'])
def create_user():
    if request.method == 'POST':
        user_name = request.json['user_name']
        email = request.json['email']
        password = pbkdf2_sha256.hash(request.json['password'])

        if user_name and email and password:
            email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            email_re_pattern = re.compile(email_pattern)

            if email_re_pattern.match(email):
                result = Ss.query(User).filter_by(email=email)

                if result.count() > 0:
                    status = [0, "this email address is already in use"]
                else:
                    user = User(
                        user_name=user_name,
                        email=email,
                        password=password
                    )
                    Ss.add(user)
                    Ss.commit()
                    Ss.close()
                    status = [1, "register successfully"]

            else:
                status = [2, "wrong email format"]

        else:
            status = [3, "don't completed input"]

        return jsonify(status)


@app.route('/auth', methods=['POST'])
def auth():
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']

        if email and password:
            user = Ss.query(User).filter_by(email=email).first()
            Ss.close()

            if user is not None and pbkdf2_sha256.verify(password, user.password) is True:
                session['user_id'] = user.user_id
                status = [1, url_for('views.index')]
            else:
                status = [0, "auth failed"]

        else:
            status = [2, "don't completed input"]

        return jsonify(status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
