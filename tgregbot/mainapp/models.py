from django.db import models


class User(models.Model):
    chat_id = models.CharField(max_length=120, unique=True)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return str(self.phone_number)
