from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.IntegerField(null=True)
    username = models.CharField(max_length=200, default='')
    firstname = models.CharField(max_length=200, default='')

class CallCount(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    button = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
