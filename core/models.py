from django.db import models
from django.conf import settings


class Question(models.Model):
    q_no = models.IntegerField()
    q_slug = models.CharField(max_length=100)
    q_text = models.CharField(max_length=255)

    DB_CHOICES = [("in", "Inventory")]
    database = models.CharField(max_length=2, choices=DB_CHOICES, default=None)

    def __repr__(self) -> str:
        return f"Question({self.q_no}. {self.q_slug[:20]}...)"

    class Meta:
        db_table = "question"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question"
    )

    dj_answer = models.TextField(max_length=1023, null=True)
    alc_answer = models.TextField(max_length=1023, null=True)
    sql_answer = models.TextField(max_length=1023, null=True)

    class Meta:
        db_table = "answer"


class AnswerCheck(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="ac_question"
    )

    dj_check = models.TextField(max_length=1023, null=True)
    alc_check = models.TextField(max_length=1023, null=True)
    sql_check = models.TextField(max_length=1023, null=True)

    class Meta:
        db_table = "anscheck"


class Solution(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="s_user"
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="s_question"
    )

    dj_answer = models.CharField(max_length=1023, null=True)
    alc_answer = models.CharField(max_length=1023, null=True)
    sql_answer = models.CharField(max_length=1023, null=True)

    class Meta:
        db_table = "solution"
