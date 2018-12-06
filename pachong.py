import requests
import time
import os
from uuid import uuid4
from settings import MONGO_DB
from settings import IMAGES_PATH, MUSIC_PATH

xmly_url = "http://m.ximalaya.com/tracks/%s.json"
url_list = [
            "/ertong/6641024/29978512","/ertong/6641024/29978514",
            "/ertong/6641024/29978519","/ertong/6641024/29978515",
            "/ertong/6641024/29978517","/ertong/6641024/29978518",
            ]
def get_content(music_id):
    url = xmly_url % (music_id)
    res = requests.get(url)
    music_dict = res.json()

    content_dict = {
        "id":music_dict.get('id'),
        "title":music_dict.get('title'),
        "album_title":music_dict.get('album_title'),
        "nickname":music_dict.get('nickname'),
        "cover":'',
        "music":'',
        'ctime':time.time(),
    }
    cover_url = music_dict.get('cover_url')
    music_url = music_dict.get('play_path')

    cover = requests.get(cover_url)# 有疑问
    music = requests.get(music_url)# 有疑问

    filename = uuid4()


    music_file_path = os.path.join(MUSIC_PATH,f'{filename}.mp3')
    cover_file_path = os.path.join(IMAGES_PATH,f'{filename}.jpg')
    print(music_file_path)

    with open(music_file_path,'wb') as f1:
        f1.write(music.content)

    with open(cover_file_path,'wb') as f2:
        f2.write(cover.content)

    content_dict['music'] = f'{filename}.mp3'
    content_dict['cover'] = f'{filename}.jpg'
    print(content_dict)
    MONGO_DB.contents.insert_one(content_dict)

for all_url in url_list:
    music_id = all_url.rsplit('/')[-1]
    get_content(music_id)