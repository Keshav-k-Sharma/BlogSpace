
from django.urls import path
from .import views 

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('stories/', views.stories, name='stories'),
]


