from django.db import models
from django.utils.translation import gettext_lazy as _
class Feedback(models.Model):
    """
    Модель для обратной связи пользователей
    """

    name = models.CharField(_("Имя"), max_length=70, null=True, blank=False)
    tel = models.CharField(
        _("Телефон"), max_length=11, null=True, blank=False
    )
    email = models.EmailField(
        _("Email"), max_length=254, null=True, blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Обратная связь")
        verbose_name_plural = _("Обратная связь")

