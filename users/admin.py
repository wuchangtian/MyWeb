from django.contrib import admin
from .models import  Post,Category,works,Comment,admin_Post
# Register your models here.
from .models import Profile
from .models import  Tag

admin.site.register(Tag)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(works)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(admin_Post)