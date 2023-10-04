from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TrainersConfig(AppConfig):
    """Default app config"""

    name = "apps.api.trainers"
    verbose_name = _("Trainers")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
