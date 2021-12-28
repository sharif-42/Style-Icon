from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import ProductBaseModel


class ProductBrand(ProductBaseModel):
    name = models.CharField(
        max_length=128,
        help_text=_("Name of the Brand"),
        unique=True
    )
    description = models.TextField(
        help_text=_("Small Description of the Brand"),
        blank=True, default="",
    )

    class Meta:
        ordering = ['-id', 'name']
        indexes = [
            models.Index(
                fields=['name', 'is_available', ]
            ),
        ]

    def __str__(self):
        return self.name
