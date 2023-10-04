from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FeedbackConfig(AppConfig):
    """Default app config"""

    name = "apps.api.feedback"
    verbose_name = _("Feedback")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
