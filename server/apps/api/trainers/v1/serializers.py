from rest_framework import serializers
from apps.api.trainers.models import Trainer
# Create your serializers here.

class TrainerSerializer(serializers.ModelSerializer):
    """Сериализатор используемых технологий"""

    class Meta:
        model = Trainer
        fields = [
            "id",
            "firstname",
            "lastname",
            "position",
            "text",
            "img",
        ]