from django.urls import path

from blog.views.comment import CommentCreate
from blog.views.home import home
from blog.views.post import PostView, PostCreate, PostUpdate, PostDelete

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', home, name='home'),

]
