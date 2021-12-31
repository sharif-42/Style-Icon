import uuid
from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import User
from cart.constants import PaymentType


class Cart(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("UUID"),
        help_text=_("This will be exposed to the outside world."),
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        help_text=_('Customer who created the cart.'),
        related_name="customers",
        null=True,
        blank=True,
    )
    total_amount = models.DecimalField(
        max_digits=15,
        decimal_places=6,
        default=Decimal("0.00"),
        verbose_name=_("Total Amount"),
        help_text=_("Total amount of the cart including all costs and VAT."),
    )
    total_amount_ex_vat = models.DecimalField(
        max_digits=15,
        decimal_places=6,
        default=Decimal("0.00"),
        verbose_name=_("Total Amount(excl. VAT)"),
        help_text=_("Total amount of the cart including all costs(excl. VAT)."),
    )
    shipping_address_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Shipping Address"),
        help_text=_("FK to the original shipping address of the customer."),
    )
    payment_type = models.CharField(
        max_length=50,
        choices=PaymentType.CHOICES,
        default=PaymentType.NONE_TYPE,
        verbose_name=_("Generic payment type"),
        help_text=_("Generic applied payment type. But remember the payment type can differ per line"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(
                fields=['payment_type',]
            ),
        ]

    def __str__(self):
        return f"Cart - {self.id}"

