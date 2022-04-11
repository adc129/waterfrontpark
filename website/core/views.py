from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'

class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blog.html'
    #fields = ('title', 'body')