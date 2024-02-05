from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=128)
    chat_id = models.CharField(max_length=120, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return str(self.username)

