from django.db import models

# Create your models here.


class Question(models.Model):
    def __str__(self):
        return self.question_text
    header = models.CharField(max_length=200, blank=True)
    question_text = models.CharField(max_length = 300)
    url = models.URLField(name=None)
    publish_date = models.DateTimeField('date published')
    answer= models.CharField(max_length=1000)
    class Meta:
        ordering = ['-id']

