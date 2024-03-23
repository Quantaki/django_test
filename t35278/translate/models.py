from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

FIELD_CHOICES = [
    ("my_choice_one", _("My choice one")),
    ("last_choice", _("Last choice")),
]
class Test(models.Model) :

    field = models.CharField(max_length=250, choices=FIELD_CHOICES )