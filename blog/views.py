from django.shortcuts import render
# from django.http import HttpResponse
from .models import Blogpost


# Create your views here.
def index(request):
    blog_data = Blogpost.objects.all().values('title', 'heading_1_content', 'pub_date', 'thumbnail', 'post_id')
    # print(blog_data)
    context = {'blog_title': blog_data}
    return render(request, 'blog/index.html', context)


def blogpost(request, blog_id):
    blog_post_data = Blogpost.objects.all().values()
    # create an objects of Blogpost class
    blog_post_data = Blogpost.objects.filter(post_id=blog_id)[0]
    # access heading_1_content class variable value.
    # print(blog_post_data.heading_1_content)
    context = {'blog_post_data': blog_post_data}
    return render(request, 'blog/blogPost.html', context)
