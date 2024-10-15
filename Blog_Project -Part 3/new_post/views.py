from django.shortcuts import render
from django.views.generic import DetailView
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import NewPostForm,NewCommentForm
from .models import NewPost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
# Create your views here.
@method_decorator(login_required,name='dispatch')
class AddPostClassView(CreateView):
    model=NewPost
    form_class=NewPostForm
    template_name='add_post.html'
    success_url=reverse_lazy("AddPost")
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author=self.request.user
        return super().form_valid(form)
@method_decorator(login_required,name='dispatch')    
class EditPostClassView(UpdateView):
    model=NewPost
    form_class=NewPostForm
    template_name='add_post.html'
    success_url=reverse_lazy("HomePage")
    pk_url_kwarg='id'
@method_decorator(login_required,name='dispatch')    
class DeletePostClassView(DeleteView):
    model=NewPost
    template_name='delete_post.html'
    success_url=reverse_lazy("HomePage")
    pk_url_kwarg='id'
class DetailPageView(DetailView):
    model=NewPost
    pk_url_kwarg='id'
    template_name='detail_page.html'
    
    def post(self, request, *args, **kwargs):
        newpost=self.get_object()
        comment_form=NewCommentForm(data=self.request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=newpost
            new_comment.save()
            return self.get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        newpost=self.object
        comments=newpost.comments.all()
        print(comments)
        print("Inside")
        print(newpost.author)
        print(self.request.user)
        comment_form=NewCommentForm() 
        context['comments']=comments
        context['comment_form']=comment_form
        return context