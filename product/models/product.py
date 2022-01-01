from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import ProductBaseModel
from .product_brand import ProductBrand
from .product_group import ProductGroup
from .product_type import ProductType


class Product(ProductBaseModel):
    name = models.CharField(
        max_length=256,
        help_text=_("Name of product.")
    )
    product_group = models.ForeignKey(
        ProductGroup,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("related product group."),
        related_name="products",
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("related product type"),
        related_name="products",
    )
    brand = models.ForeignKey(
        ProductBrand,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("related product brand"),
        related_name="products",
    )
    in_stock = models.PositiveIntegerField(
        default=0,
        help_text=_("Amount of available products.")
    )
    short_description = models.TextField(
        help_text=_("Short summary, can be used in search results."),
        blank=True,
        default="",
    )
    long_description = models.TextField(
        help_text=_("Long Description"),
        blank=True,
        default=""
    )
    weight = models.DecimalField(
        max_digits=13,
        decimal_places=3,
        blank=True,
        null=True,
        help_text=_(
            "Default weight of product in grams. "
        ),
    )
    release_date = models.DateField(
        blank=True,
        null=True,
        help_text=_("Release date. Product release on date, can be used for taking pre-orders."),
    )
    pre_order = models.BooleanField(
        default=False,
        verbose_name=_("Is pre-order product"),
        help_text=_('Can be pre ordered')
    )
    is_serviceable = models.BooleanField(
        default=False,
        help_text=_("Is the product serviceable")
    )
    service_period = models.IntegerField(
        default=0,
        help_text=_("Service Period in Months. How long user get free service."),
        verbose_name=_("Service Period in Months."),
    )
    valid_from = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Valid from"),
        help_text=_("Enter the datetime from which the product is valid"),
    )
    valid_until = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Valid until"),
        help_text=_("Enter the datetime on which the product's validity expires"),
    )
    # image_thumbnail = models.ImageField(
    #     upload_to="product_images/%Y/%m/%d/",
    #     max_length=500,
    #     verbose_name=_("Thumbnail image"),
    #     help_text=_("Use this for the thumbnail"),
    #     blank=True,
    #     null=True
    # )
    # image_alternative_1 = models.ImageField(
    #     upload_to="product_images/%Y/%m/%d/",
    #     max_length=500,
    #     verbose_name=_("Alternative image 1"),
    #     help_text=_("Additional image"),
    #     blank=True,
    #     null=True
    # )
    # image_alternative_2 = models.ImageField(
    #     upload_to="product_images/%Y/%m/%d/",
    #     max_length=500,
    #     verbose_name=_("Alternative image 2"),
    #     help_text=_("Additional image"),
    #     blank=True,
    #     null=True
    # )
    # image_alternative_3 = models.ImageField(
    #     upload_to="product_images/%Y/%m/%d/",
    #     max_length=500,
    #     verbose_name=_("Alternative image 3"),
    #     help_text=_("Additional image"),
    #     blank=True,
    #     null=True
    # )
    # image_alternative_4 = models.ImageField(
    #     upload_to="product_images/%Y/%m/%d/",
    #     max_length=500,
    #     verbose_name=_("Alternative image 4"),
    #     help_text=_("Additional image"),
    #     blank=True,
    #     null=True
    # )

    class Meta:
        ordering = ['-id', 'name']
        indexes = [
            models.Index(
                fields=['code', 'name', 'product_group', 'product_type', 'brand', 'in_stock']
            ),
        ]

    def __str__(self):
        return self.name
