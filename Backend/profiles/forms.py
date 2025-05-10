from profiles.models import Liste_des_demandes,add_prodact,pixlfb,Liste_storecharging,interfacewebsite,Livraison,Liste_des_commandes,wilaya
from django.forms import ModelForm
from django import forms
from client.models import Client, Domain
from django.contrib.auth.models import User

from django_tenants.utils import schema_context

from sweet_shared.models import sahlaboost,add_payments











from django.forms import ModelForm

from .models import Liste_des_demandes,add_prodact,Liste_des_commandes

from functools import partial

from django import forms
from django.contrib.auth.models import User

from django import forms
from client.models import Client, Domain


from sweet_shared.models import SweetType,confirmserial,Payments,coliinformation,Confirmerlidentite,domainn


from django_tenants.utils import schema_context



from django.contrib.auth import get_user_model






class CustomerForm(ModelForm):

	
	class Meta:
		model = Liste_des_commandes
		fields = '__all__'















class Addproduct(ModelForm):
	
	class Meta:
		model = add_prodact
		fields = '__all__'		










class Livraisonform(ModelForm):
	
	class Meta:
		model = Livraison
		fields = '__all__'	




class wilayaform(ModelForm):
	
	class Meta:
		model = wilaya
		fields = '__all__'	












class Listeorders(ModelForm):
	
	class Meta:
		model = Liste_des_demandes
		fields = '__all__'	






class OpenStoreForm(forms.Form):

  
   

    username = forms.CharField(max_length=150)
    email = forms.EmailField( required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    domain = forms.CharField(max_length=100)

    def save(self):
        with schema_context('public'):
	        # إنشاء النطاق الفرعي
            tenant = Client(schema_name=self.cleaned_data['name'], name=self.cleaned_data['name'])
            tenant.save()
	    

            # إنشاء المستخدم الفائق
            user = User.objects.create_superuser(
             username=self.cleaned_data['username'],
             email=self.cleaned_data['email'],
             password=self.cleaned_data['password']
            )

          


            # ربط النطاق الفرعي بالمستأجر
            domain = Domain(domain=self.cleaned_data['domain'], tenant=tenant, is_primary=True)
            domain.save()











class OpenStore(forms.Form):
    
    name = forms.CharField(max_length=100, required=False )
    domain = forms.CharField(max_length=100)

   
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
    email = forms.CharField(max_length=120, required=False)

    wilaya = forms.CharField(max_length=120)
    address = forms.CharField(max_length=120)
    phonenumber= forms.CharField(max_length=120)


    def save(self):
     with schema_context('public'):
        # إنشاء المستأجر
        tenant = Client(schema_name=self.cleaned_data['name'], name=self.cleaned_data['name'])
        tenant.save()

        # ربط النطاق بالمستأجر
        domain = Domain(domain=self.cleaned_data['domain'], tenant=tenant, is_primary=True)
        domain.save()

    # استخراج اسم المستخدم
     username = self.cleaned_data['username']

    # ✅ تحقق إذا كان اسم المستخدم مسجل من قبل في SweetType
     if SweetType.objects.filter(username=username).exists():
        print("اسم المستخدم موجود بالفعل. لم يتم حفظه.")  # أو سجل رسالة في اللوج فقط
        return  # ما تحفظ والو

    # ✅ إذا ماكانش مسجل، احفظ المعلومات
     sweet_type = SweetType(
        name=self.cleaned_data['name'],
        username=username,
        password=self.cleaned_data['password'],
        email=self.cleaned_data['email'],
        domainname=self.cleaned_data['domain'],
        wilaya=self.cleaned_data['wilaya'],
        address=self.cleaned_data['address'],
        phonenumber=self.cleaned_data['phonenumber'],
     )
     sweet_type.save()







class CreateTenantForm(forms.Form):
    name = forms.CharField(max_length=100)
    domain = forms.CharField(max_length=100)

    def save(self):
        tenant = Client(schema_name=self.cleaned_data['name'], name=self.cleaned_data['name'])
        tenant.save()

        domain = Domain(domain=self.cleaned_data['domain'], tenant=tenant, is_primary=True)
        domain.save()

        return tenant











class CreateTenantSuperuserForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_superuser(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user
    
class ConfirmSerialForm(forms.ModelForm):
    class Meta:
        model = confirmserial
        fields = ['username', 'serial', 'confirmserial']


class PixlfbForm(forms.ModelForm):
    class Meta:
        model = pixlfb
        fields = ['namepixel', 'idpixel']







class Storecharging(ModelForm):
	
	class Meta:
		model = Liste_storecharging
		fields = '__all__'						








class interfacewebsiteForm(ModelForm):

	
	class Meta:
		model = interfacewebsite
		fields = '__all__'











class YourDomainForm(ModelForm):

	
	class Meta:
		model = domainn
		fields = '__all__'



class PaymentForm(forms.ModelForm):
    class Meta:
        model = add_payments
        fields = '__all__'









from django import forms

class TenantLoginForm(forms.Form):
    domain = forms.CharField(label='Domain')
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)





class sahlaboostForm(forms.ModelForm):
    class Meta:
        model = sahlaboost
        fields = '__all__'














from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    
    password = forms.CharField(widget=forms.PasswordInput, required=True)





class SweetTypeForm(forms.ModelForm):
    class Meta:
        model = SweetType
        fields = '__all__' 











from django import forms

from sweet_shared.models import activation_money_book

class ActivationForm(forms.ModelForm):
    class Meta:
        model = activation_money_book
        fields = ['conferm_serial']  # عرض حقل 'conferm_serial' فقط في النموذج
        labels = {
            'conferm_serial': 'Confirm Serial Number',  # تخصيص التسمية
        }
        widgets = {
            'conferm_serial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Serial Number'}),
        }