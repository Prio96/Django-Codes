# from django.forms import BaseModelForm
# from django.http import HttpResponse
# from django.shortcuts import render,redirect
# from .forms import NewPostForm,NewCommentForm
# from .models import NewPost
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
# from django.urls import reverse_lazy
# Create your views here.
# @login_required
# def AddPost(request):
#     if request.method=='POST':
#         form=PostForm(request.POST)
#         if form.is_valid():
#             form.instance.author=request.user
#             print(form.cleaned_data)
#             form.save()
#             return redirect("AddPost")
#     else:
#         form=PostForm()
#     return render(request,'add_post.html',{'form':form})
# @login_required
# def EditPost(request,id):
#     post=Post.objects.get(pk=id)
#     form=PostForm(instance=post)
#     if request.method=='POST':
#         form=PostForm(request.POST,instance=post)
#         if form.is_valid():
#             form.instance.author=request.user
#             print(form.cleaned_data)
#             form.save()
#             return redirect("HomePage")
#     return render(request,'add_post.html',{'form':form})
# @login_required
# def DeletePost(request,id):
#     post=Post.objects.get(pk=id)
#     post.delete()
#     return redirect("HomePage")
# @method_decorator(login_required,name='dispatch')
# class AddPostClassView(CreateView):
#     model=Post
#     form_class=PostForm
#     template_name='add_post.html'
#     success_url=reverse_lazy("AddPost")
#     def form_valid(self, form: BaseModelForm) -> HttpResponse:
#         form.instance.author=self.request.user
#         return super().form_valid(form)
# @method_decorator(login_required,name='dispatch')    
# class EditPostClassView(UpdateView):
#     model=Post
#     form_class=PostForm
#     template_name='add_post.html'
#     success_url=reverse_lazy("HomePage")
#     pk_url_kwarg='id'
# @method_decorator(login_required,name='dispatch')    
# class DeletePostClassView(DeleteView):
#     model=NewPost
#     template_name='delete_post.html'
#     success_url=reverse_lazy("HomePage")
#     pk_url_kwarg='id'

# class DetailPageView(DetailView):
#     model=Post
#     pk_url_kwarg='id'
#     template_name='detail_page.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         post=self.object
#         comments=post.comments.all()
#         print(comments)
#         if self.request.method=='POST':
#             comment_form=CommentForm(self.request.POST)
#             if comment_form.is_valid():
#                 new_comment=comment_form.save(commit=False)
#                 new_comment.post=post
#                 new_comment.save()
#         else:
#             print("Inside")
#             comment_form=CommentForm()
        
#         context['comments']=comments
#         context['comment_form']=comment_form
#         return context
        
        
    