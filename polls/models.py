from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    created_to = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice_text


class StaticFileTest(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/images/")


    def __str__(self):
        return self.title