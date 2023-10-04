from rest_framework import views
from apps.api.feedback.models import Feedback
from rest_framework.generics import CreateAPIView
from .serializers import FeedbackSerializer


class FeedbackAPICreate(CreateAPIView):
    
    serializer_class = FeedbackSerializer
