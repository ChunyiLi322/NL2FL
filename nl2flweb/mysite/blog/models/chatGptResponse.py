from django.db import models
from django.contrib.auth.models import User


class ChatGptResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    key_words = models.CharField(max_length=200)
    ltl = models.CharField(max_length=9999)
    ltl_parse = models.CharField(max_length=9999)
    pub_date = models.DateTimeField('date published', auto_now_add=True)


