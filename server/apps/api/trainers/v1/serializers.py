from rest_framework import serializers
from apps.api.trainers.models import Trainer, Social
# Create your serializers here.


class SocialsSerializer(serializers.ModelSerializer):
      class Meta:
        model = Social
        fields = [
            "id",
            "name",
            "icon",
            "link",
        ]


class TrainerSerializer(serializers.ModelSerializer):
    """Сериализатор используемых технологий"""
    socials = SocialsSerializer(many=True)
    class Meta:
        model = Trainer
        fields = [
            "id",
            "socials",
            "firstname",
            "lastname",
            "position",
            "text",
            "img",
        ]