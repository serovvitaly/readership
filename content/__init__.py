from django.shortcuts import render


def get_post(request, post_id):
    return render(request, 'content/post.html', {'post_id': post_id})


def get_posts_list(request):
    from . import models
    posts_list = models.Article.objects.all()[:31]
    posts_images = []
    posts_ids = []
    for post in posts_list:
        posts_ids.append(post.id)
    print(posts_ids)
    #imgs = models.Image.objects.filter(article_id__in=posts_ids)
    #print(imgs)
    return render(request, 'content/posts_list.html', {'posts_list': posts_list, 'posts_images': posts_images})
