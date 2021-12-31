from django.utils.translation import gettext_lazy as _


class PaymentType:
    NONE_TYPE = "none"
    CASH_ON_DELIVERY = "cash on delivery"
    DIGITAL = "digital"

    CHOICES = (
        (NONE_TYPE, _("User defined")),
        (CASH_ON_DELIVERY, _("Cash on delivery")),
        (DIGITAL, _("Digital")),
    )
