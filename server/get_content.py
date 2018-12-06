from flask import Blueprint,jsonify
from settings import MONGO_DB

content = Blueprint('content',__name__)

@content.route('/content_list/',methods=['POST'])
def content_list():
    content_list = list(MONGO_DB.contents.find({}))
    for index,item in enumerate(content_list):
        content_list[index]['_id'] = str(content_list[index]['_id'])
    return jsonify(content_list)
