from django.contrib import admin
from .models import Topics, LikesDislikes, Comments
# Register your models here.
admin.site.register(Topics)
admin.site.register(LikesDislikes)
admin.site.register(Comments)

