from django.contrib import admin
from App_Teacher.models import *
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Replay)
admin.site.register(Likes)
admin.site.register(Quiz)
admin.site.register(AnswerList)