import lib.vk as vk
from pymongo import MongoClient

group_domain = 'space_live'
items_on_page = 100
offset = 0

request = vk.request('wall.get')
request.set_param('domain', group_domain)
request.set_param('offset', offset)
request.set_param('count', items_on_page)

list = vk.list(request)
list.exec()


items = list.get_items()

print(len(items))


client = MongoClient('mongodb://localhost/')
db = client.vk
posts = db.posts

#for post in items:
    #post['group_domain'] = group_domain
    #posts.insert(post)


