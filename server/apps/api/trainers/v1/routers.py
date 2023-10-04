from django.urls import path
from .views import TrainerAPIList, TrainerAPIRetrieve
app_name = "trainers"

urlpatterns = [
    path("list/", TrainerAPIList.as_view(), name="trainers"),
    path('<int:pk>', TrainerAPIRetrieve.as_view()),
]
