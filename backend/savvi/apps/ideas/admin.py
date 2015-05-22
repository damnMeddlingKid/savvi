from django.contrib import admin
from .models import Idea
from .models import Comment

admin.site.register(Idea)
admin.site.register(Comment)
