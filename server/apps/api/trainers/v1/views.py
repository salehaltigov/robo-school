from apps.api.trainers.models import Trainer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from .serializers import TrainerSerializer
class TrainerAPIList(ListAPIView):
    
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.order_by("order")

class TrainerAPIRetrieve(RetrieveUpdateAPIView):
    
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.order_by("order")