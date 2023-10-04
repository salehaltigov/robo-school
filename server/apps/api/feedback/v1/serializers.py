from rest_framework import serializers

from apps.api.feedback.models import Feedback
# Create your serializers here.

class FeedbackSerializer(serializers.ModelSerializer):
    """Сериализатор используемых технологий"""

    class Meta:
        model = Feedback
        fields = [
            "id",
            "name",
            "email",
            "tel",            
        ]
