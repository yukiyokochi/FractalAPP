from django.contrib import admin
from .models import Blog, Category, Comment, Tag

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)

# Register your models here.
