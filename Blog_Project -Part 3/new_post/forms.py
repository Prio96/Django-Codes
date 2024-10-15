from django import forms
from .models import NewPost,NewComment

class NewPostForm(forms.ModelForm):
    class Meta:
        model=NewPost
        exclude=['author']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model=NewComment  
        fields=['name','email','body']