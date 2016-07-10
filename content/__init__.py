from django.shortcuts import render


def get_post(request, post_id):
    return render(request, 'content/post.html', {'post_id': post_id})


def get_posts_list(request):
    from . import models
    posts_list = models.Article.objects.all()
    return render(request, 'content/posts_list.html', {'posts_list': posts_list})
