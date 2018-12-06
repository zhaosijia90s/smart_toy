import os

from flask import Blueprint
from flask import send_file

from settings import IMAGES_PATH
from settings import MUSIC_PATH

get_sth = Blueprint('get_sth',__name__)

@get_sth.route('/get_imgs/<filename>')
def get_imgs(filename):
    img_file_name = os.path.join(IMAGES_PATH,filename)
    return send_file(img_file_name)

@get_sth.route('/get_musics/<filename>')
def get_musics(filename):
    music_file_name = os.path.join(MUSIC_PATH,filename)
    return send_file(music_file_name)