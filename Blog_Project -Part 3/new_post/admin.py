from django.contrib import admin
from .models import NewComment,NewPost
# Register your models here.
admin.site.register(NewPost)
admin.site.register(NewComment)