from __future__ import unicode_literals
import datetime


from django.db import models
from django.utils import timezone


class Food(models.Model):
    food_text = models.CharField(max_length=200
    	)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.food_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default='SOME STRING')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text