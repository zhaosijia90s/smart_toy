import pymongo

#数据库配置
mongo = pymongo.MongoClient(host='127.0.0.1',port=27017)
MONGO_DB = mongo['wanju']

#数据存放目录
IMAGES_PATH = 'images'
MUSIC_PATH = 'music'
AVATAR_PATH = 'avatar'

#前后端交互数据
RET = {
    'code':0,
    'msg':'',
    'data':{}
}