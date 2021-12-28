from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import ProductBaseModel
from product.constants import ProductItemType


class ProductType(ProductBaseModel):
    name = models.CharField(
        max_length=128,
        help_text=_("Name of the Product Type."),
        unique=True
    )
    description = models.TextField(
        help_text=_("Description of the Product Type."),
        blank=True, default="",

    )
    system_type = models.CharField(
        max_length=20,
        choices=ProductItemType.CHOICES,
        default=ProductItemType.NONE_TYPE,
    )

    class Meta:
        ordering = ['-id', 'name', 'system_type']
        indexes = [
            models.Index(
                fields=['name', 'is_available', 'system_type', ]
            ),
        ]

    def __str__(self):
        return self.name
