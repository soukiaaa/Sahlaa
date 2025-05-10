from django.contrib import admin
from .models import Profile
from .models import Order_accounts
from .models import *
from client.models import *




@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['user', 'bio', 'created']




class list_Order_accounts(admin.ModelAdmin):
    list_display=['user','total_Order','en_circuit','livrer','recouverts','message']
admin.site.register(Order_accounts,list_Order_accounts) 





admin.site.register(userprofail)   
admin.site.register(Commandes)
admin.site.register(pixlfb)


admin.site.register(Client)
admin.site.register(Domain)

admin.site.register(Tenant)


admin.site.register(coverwebsite)
admin.site.register(header)
admin.site.register(add_prodact)
admin.site.register(Liste_des_demandes)

admin.site.register(Liste_des_commandes)


admin.site.register(Listecommandi)


admin.site.register(interfacewebsite)

admin.site.register(wilaya)
admin.site.register(Livraison)




admin.site.register(statu)




admin.site.register(video)