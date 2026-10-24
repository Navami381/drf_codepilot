from django.db import models
from exams.models import AssessmentModel
from accounts.models import User

# Create your models here.
class QuestionModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    score=models.PositiveIntegerField()
    assessment=models.ForeignKey(AssessmentModel,on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    sample_input=models.TextField(null=True)
    sample_output=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)