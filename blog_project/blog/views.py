from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def list_posts(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'list_posts.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_details.html', {'post': post})
