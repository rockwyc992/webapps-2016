from django.db import models
import random

class Shortener(models.Model):
    def new_url():
        length = 1
        chars = '0123456789'
        chars += 'abcdefghijklmnopqrstuvwxyz'
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        id = ''
        tries = 0
        while True:
            if tries > 2:
                length += 1
            id = ''
            for i in range(0, length):
                id += random.choice(chars)
            print(id)
            if Shortener.objects.filter(short_url=id):
                tries += 1
                continue
            else :
                break
        return id

    long_url = models.URLField(max_length=8192)
    short_url = models.CharField(max_length=200, default=new_url)
    click = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

