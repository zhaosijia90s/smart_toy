l1 = ["1","2","3","4","5"]
a = '*'.join(l1)
# print(a)

import os
# path = os.path.join('/indes/','login')
# print(path)
from settings import MONGO_DB

content = MONGO_DB.contents.find({})
print(content)