from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost,Author
# Create your views here.

def index(request,page_num=1):
    start = page_num*5 - 5
    end = page_num*5
    latest_posts = BlogPost.objects.order_by('-date')[start:end]
    return render(request,"blog/index.html",context={"latest_posts":latest_posts,"next":page_num+1})

def entry(request, blogpost_title):
    blogpost  = get_object_or_404(BlogPost, title=blogpost_title).content
    return render(request,"blog/entry.html",context= {"blogpost":blogpost})
