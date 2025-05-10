# Create your models here.
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
#User = get_user_model()





#class Client(TenantMixin):

  #  name = models.CharField(max_length=100)
   
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    # default true, schema will be automatically created and synced when it is saved
   # auto_create_schema = True




  #  name = models.CharField(max_length=100)
    #owner = models.OneToOneField(User, on_delete=models.CASCADE)
  #  auto_create_schema = True





#class Domain(DomainMixin):
  #  pass





#class Client(TenantMixin):
#    name = models.CharField(max_length=100)
   # owner = models.OneToOneField(User, on_delete=models.CASCADE)
#    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

#    auto_create_schema = True

#class Domain(DomainMixin):
#    pass

# نموذج Tenant الجديد
#class Tenant(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    domain = models.CharField(max_length=255)


from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    auto_create_schema = True

class Domain(DomainMixin):
    pass

class Tenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
