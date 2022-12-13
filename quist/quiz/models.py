from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"