from django.urls import path
from exams.views import AssessmentCreateListView,AssessmentRetriveUpdateDeleteView

urlpatterns=[
    path("assessment/",AssessmentCreateListView.as_view()),
    path("assessment/<int:pk>/",AssessmentRetriveUpdateDeleteView.as_view())
]