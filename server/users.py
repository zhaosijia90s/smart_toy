from flask import Blueprint,request,jsonify

from settings import MONGO_DB
from settings import RET
from settings import AVATAR_PATH


user_info = Blueprint('user_info',__name__)

@user_info.route('/regist/',methods=['POST'])
def regist():
    username = request.form.get('username')
    password = request.form.get('password')
    nickname = request.form.get('nickname')
    phone = request.form.get('phone')
    gender = request.form.get('gender')

    user = {
        'username': username,
        'password': password,
        'nickname': nickname,
        'phone': phone,
        'gender': int(gender),
        'avatar': 'boy.jpg' if int(gender) == 1 else 'girl.jpg',
        'bind_toy': [],
        'frind_list': []
    }
    MONGO_DB.users.insert_one(user)

    RET['code'] = 1,
    RET['msg'] = '注册成功！',
    RET['data'] = {},
    return jsonify(RET)

