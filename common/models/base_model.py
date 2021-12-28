import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models.user import User


class LogBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_('who created.'),
        related_name='creator',
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_('who updated.'),
        related_name='updator',
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class ProductBaseModel(LogBase):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("UUID"),
        help_text=_("This will be exposed to the outside world."),
    )
    code = models.CharField(
        max_length=128, unique=True, help_text=_("Unique reference given by the author.")
    )
    is_available = models.BooleanField(
        default=False, help_text=_("If TRUE, then record is available")
    )

    class Meta:
        abstract = True


