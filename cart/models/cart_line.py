import uuid
from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _

from cart.models import Cart
from product.services import ProductService


class CartLine(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("UUID"),
        help_text=_("This will be exposed to the outside world."),
    )
    cart = models.ForeignKey(
        Cart,
        related_name="lines",
        on_delete=models.CASCADE,
        verbose_name=_("Cart"),
        help_text=_("To which cart this line belongs to."),
    )
    product_code = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name=_("Product Code"),
        help_text=_("Product code."),
    )
    product_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_("Product Name"),
        help_text=_("Name of product."),
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name=_("Quantity"),
        help_text=_("Quantity of product."),
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        default=Decimal("0.00"),
        verbose_name=_("Price"),
        help_text=_("Price per product. This is the unit price of the product."),
    )
    price_ex_vat = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        default=Decimal("0.00"),
        verbose_name=_("Price(excl. VAT)"),
        help_text=_("Price(excl. VAT) per product. This is the unit price(excl. VAT) of the product."),
    )
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        default=Decimal("0.00"),
        verbose_name=_("Total Amount"),
        help_text=_("Total amount of the line."),
    )
    total_amount_ex_vat = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        default=Decimal("0.00"),
        verbose_name=_("Total Amount(excl. VAT)"),
        help_text=_("Total amount(excl. VAT) of the line."),
    )

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(
                fields=['uuid', 'product_code']
            ),
        ]

    def __str__(self):
        return str(self.uuid)

    def save(self, *args, **kwargs):
        self.product_name = ProductService().get_product_name_by_product_code(product_code=self.product_code)
        # TODO: calculate total amount, total amount ex vat, get product name, price etc
        super().save(*args, **kwargs)
