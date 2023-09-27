from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post

def home(request):
    return render(request, 'main/home.html', {})


class PostListView(ListView):
    model = Post
    template_name = 'main/home.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name ='main/create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
