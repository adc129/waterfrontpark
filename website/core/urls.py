"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import DeleteBlogView, HomeView, BlogDetailView, AddBlogView, UpdateBlogView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="blog-details"),
    path('add_post/', AddBlogView.as_view(), name="add_post"),
    path('post/<int:pk>/comment ', AddCommentView.as_view(), name="add_comment"),
    path('post/edit/<int:pk>', UpdateBlogView.as_view(), name="update_post"),
    path('post/delete/<int:pk>', DeleteBlogView.as_view(), name="delete_post"),
    path('like/<int:pk>', LikeView, name='like_post'),
]
