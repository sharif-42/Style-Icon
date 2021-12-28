from django.utils.translation import gettext_lazy as _


class ProductItemType:
    NONE_TYPE = "none"
    HANDSET = "handset"
    TABLET = "tablet"

    CHOICES = (
        (NONE_TYPE, _("User defined")),
        (HANDSET, _("Handset")),
        (TABLET, _("Tablet")),
    )
