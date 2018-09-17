from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    class Meta:
        db_table = 'question'

    question_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField('data published')

    def __repr__(self):
        return '{}{}'.format(self.question_text,self.pub_date)

    __str__ = __repr__

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    class Meta:
        db_table = 'choice'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __repr__(self):
       return '{}{}{}'.format(self.choice_text,self.choice_text,self.votes)