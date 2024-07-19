from django.db import models
from django.conf import settings


class Question(models.Model):
    q_no = models.IntegerField()
    q_text = models.CharField(max_length=255)

    DB_CHOICES = [("IN", "Inventory")]
    database = models.CharField(max_length=2, choices=DB_CHOICES, default=None)

    class Meta:
        db_table = "question"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question")

    dj_answer = models.CharField(max_length=1023, null=True)
    alc_answer = models.CharField(max_length=1023, null=True)
    sql_answer = models.CharField(max_length=1023, null=True)

    class Meta:
        db_table = "answer"


class Solution(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    dj_answer = models.CharField(max_length=1023, null=True)
    alc_answer = models.CharField(max_length=1023, null=True)
    sql_answer = models.CharField(max_length=1023, null=True)

    class Meta:
        db_table = "solution"
