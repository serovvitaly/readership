import lib.vk as vk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost/')
db = client.vk
posts = db.posts.find({'comments.count': {'$gt': 0}})
comments = db.comments

comments_count = 0
comments_find_count = 0
posts_count = posts.count()
post_counter = 0

for post in posts:
    post_counter += 1
    request = vk.request('wall.getComments')
    request.set_param('owner_id', post['owner_id'])
    request.set_param('post_id', post['id'])
    request.set_param('count', 100)
    list = vk.list(request)
    list.exec()
    items = list.get_items()
    comments.insert_many(items)

    print(str(post_counter) + ' из ' + str(posts_count) + ' Должно быть: ' + str(post['comments']['count']) + ', найдено: ' + str(len(items)))
    comments_count += post['comments']['count']
    comments_find_count += len(items)

print('Общее количество найденных: ' + str(comments_find_count) + ' из ' + str(comments_count))
