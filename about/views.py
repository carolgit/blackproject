from django.shortcuts import get_object_or_404, render
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def post_content(request, pk=1):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_content.html", {'post':post})

@login_required
def post_private(request):
    return render(request, "post_private.html")