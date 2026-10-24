from django.db import models
from accounts.models import User

# Create your models here.
class AssessmentModel(models.Model):
    LANGUAGE_CHOICES=[
        ("python","python"),
        ("C","C"),
        ("java","java"),
        ("sql","sql")
        
    ]

    STATUS_CHOICES = [
    ('Draft', 'Draft'),
    ('Scheduled', 'Scheduled'),
    ('Published', 'Published'),
    ('Ongoing', 'Ongoing'),
    ('Completed', 'Completed'),
    ('Archived', 'Archived'),
    ]
    title=models.CharField(max_length=200)
    batch=models.CharField(max_length=100)
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default=("python"))
    exam_date=models.DateTimeField()
    start_time=models.TimeField()
    duration=models.PositiveIntegerField()
    end_time=models.TimeField(null=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default=("Draft"))

    def __str__(self):
        return f"{self.title}"
