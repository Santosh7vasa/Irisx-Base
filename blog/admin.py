from django.contrib import admin
from .models import Post
from .models import Language, Device
# Register your models here.

admin.site.register(Post)
admin.site.register(Language)
admin.site.register(Device)
