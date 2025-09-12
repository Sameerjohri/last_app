from django.contrib import admin # type: ignore
from .models import Post,Member

# Register your models here.

admin.site.register(Post)

admin.site.register(Member)