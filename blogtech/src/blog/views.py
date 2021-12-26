from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BlogPost
from django.contrib.auth.decorators import login_required


class BlogPostHomeView(ListView):
    model = BlogPost
    context_object_name = "posts"


class BlogPostDetailsView(DetailView):
    model = BlogPost
    context_object_name = "post"

@method_decorator(login_required, name='dispatch')
class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'image','author', 'category', 'content']

    def get_success_url(self):
        return reverse('posts:home')

@method_decorator(login_required, name='dispatch')
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author', 'category', 'content']
    template_name = 'blog/blogpost_update.html'

@method_decorator(login_required, name='dispatch')
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('posts:home')