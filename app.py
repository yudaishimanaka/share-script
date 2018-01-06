from flask import *
from views import views
from database import Session as Ss
from models import *
from passlib.hash import pbkdf2_sha256
import re


app = Flask(__name__)

app.register_blueprint(views.views)


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
                    status = jsonify([0, "this email address is already in use"])
                else:
                    user = User(
                        user_name=user_name,
                        email=email,
                        password=password
                    )
                    Ss.add(user)
                    Ss.commit()
                    Ss.close()
                    status = jsonify([1, "register successfully"])

            else:
                status = jsonify([2, "wrong email format"])

        else:
            status = jsonify([3, "don't completed input"])

        return status


@app.route('/auth', methods=['POST'])
def auth():
    if request.method == "POST":
        email = request.json['email']
        password = request.json['password']
        return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
