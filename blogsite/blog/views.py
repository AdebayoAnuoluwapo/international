from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import forms
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class HomeView(TemplateView):
    template_name = 'blog/index.html'


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    


       

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'registration/signup.html'

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/blog/login')
        else:
            return render(request, self.template_name, {'form':form})


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    model = Post
            
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = '/login/'
    form_class = forms.PostForm
    redirect_field_name = 'blog/post_detail.html'

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'blog/post_detail.html'
    model = Post    

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Post
    success_url = reverse_lazy('blog:list')



# funstions That require PK
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:detail', pk=pk)

@login_required
def add_comment_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post =  post
            comment.save()
            return redirect('blog:detail', pk=pk)
    else:
        form = forms.CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})


