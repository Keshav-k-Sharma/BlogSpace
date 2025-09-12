from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render , redirect

# --------------------------
# API Views (for JSON access)
# --------------------------
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


# --------------------------
# Template Views (for frontend pages)
# --------------------------
def index(request):
    return render(request, "index.html")

def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('index')  # must match name in urls.py
    return render(request, 'write.html')





def stories(request):
    return render(request, "stories.html")

