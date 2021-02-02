from django.db import models
from random import randint


class Tokens(models.Model):
    token = models.CharField(max_length=32)
    permissions = models.IntegerField(max_length=1)

class Devices(models.Model):
    name = models.CharField(max_length=18)
    device_key = models.IntegerField(max_length=4)
    device_token = models.CharField(max_length=32)

    def set_token(self):
        generated_token = ""
        for __ in range(16):
            generated_token += hex(randint(0, 255))[2:].rjust(2, "0")
        self.device_token = generated_token
