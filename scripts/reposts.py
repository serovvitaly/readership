import lib.vk as vk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost/')
db = client.vk
posts = db.posts.find({'reposts.count': {'$gt': 0}})
reposts = db.reposts

for post in posts:
    request = vk.request('wall.getReposts')
    request.set_param('owner_id', post['owner_id'])
    request.set_param('post_id', post['id'])
    response = request.exec().get_response().get_response()
    reposts.insert_many(response['items'])
