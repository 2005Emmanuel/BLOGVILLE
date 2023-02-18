from django.contrib import admin
from .models import Profile
from.models import Blogpost
from .models import Comment
from .models import Follower_Following
# from .models import Like_Unlike
# Register your models here.
@admin.register(Profile)
class registerAdmin(admin.ModelAdmin):
 raw_id_fields = ['user']
admin.site.register(Blogpost)
admin.site.register(Comment)
admin.site.register(Follower_Following)
# admin.site.register(Like_Unlike)
