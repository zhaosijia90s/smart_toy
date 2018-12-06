from flask import Flask
from server import get_content,get_sth,users
app = Flask(__name__)
app.register_blueprint(get_content.content)
app.register_blueprint(get_sth.get_sth)
app.register_blueprint(users.user_info)

if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)