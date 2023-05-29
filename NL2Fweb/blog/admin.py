from django.contrib import admin

from blog.models.chatGptResponse import ChatGptResponse
from blog.models.formalMethod import FormalMethod
from blog.models.keyWord import KeyWord
from blog.models.comment import Comment
from blog.models.post import Post


USERNAME_JOHN = 'john_lennon'
PASSWORD_JOHN = 'john_password'

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ChatGptResponse)
admin.site.register(FormalMethod)
admin.site.register(KeyWord)