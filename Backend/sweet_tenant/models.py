from django.db import models

# Create your models here.
from sweet_shared.models import SweetType

class Sweet(models.Model):
    sweetype= models.ForeignKey(SweetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    