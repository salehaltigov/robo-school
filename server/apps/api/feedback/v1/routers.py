from django.urls import path
from .views import FeedbackAPICreate

app_name = "feedback"

urlpatterns = [
    path("create/", FeedbackAPICreate.as_view()),
]
