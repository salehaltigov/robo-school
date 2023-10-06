from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SocialIconsChoices(models.TextChoices):
    FACEBOOK = "mdi-facebook", _("Facebook"),
    INSTAGRAM = "mdi-instagram", _("Instagram")
class Trainer(models.Model):

    firstname = models.CharField(
        _("Имя"), unique=True, max_length=30, blank=False, null=False,
    )
    lastname = models.CharField(
        _("Фамилия"), unique=True, max_length=30, blank=False, null=False,
    )
    img = models.ImageField(
        blank=True, null=True, verbose_name=_("Фотография")
    )
    position = models.CharField(
        _("Должность"), max_length=30, blank=False, null=False,
    )
    text = RichTextUploadingField(_("Подробная информация"))
    order = models.PositiveIntegerField(
        _("Порядок вывода"), null=True, blank=True
    )
    class Meta:
        verbose_name = _("Преподаватель")
        verbose_name_plural = _("Преподаватели")


class Social(models.Model):
    """
    Социальные сети пользователя
    """
    trainer = models.ForeignKey(
        Trainer,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="socials"
    )
    name = models.CharField(
        _("Наименование"), max_length=50, null=True, blank=True,
    )

    icon = models.CharField(
        _("Иконка"),
        max_length=50,
        help_text="Необходим класс mdi",
        null=True,
        blank=True,
        choices= SocialIconsChoices.choices
    )

    link = models.URLField(
        _("Ссылка на социальную сеть"), max_length=200, null=True, blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Социальная сеть пользователя")
        verbose_name_plural = _("Социальные сети пользователя")