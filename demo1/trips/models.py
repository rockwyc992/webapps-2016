from django.db import models

# Create your models here.

class List(models.Model):
    homework = models.IntegerField(default=1)
    problem = models.IntegerField()
    def __str__(self):
        return 'Ph%d %d' % (self.homework, self.problem)
