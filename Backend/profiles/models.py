from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
from django.utils import timezone



















class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='Profile', default='default.png')
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)



class userprofail(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    confermPassword=models.CharField(max_length=110)
    namesite=models.CharField(max_length=110)
    def __str__(self):
        return self.user.username         



class Order_accounts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_Order =models.CharField(max_length=110)
    en_circuit=models.CharField(max_length=110)
    livrer=models.CharField(max_length=110)
    recouverts=models.CharField(max_length=110)
    message=models.CharField(max_length=110)
    def __str__(self):
        return self.user.username         






class Commandes(models.Model):
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Nom_Complet  =models.CharField(max_length=110)
    Mobile_1=models.CharField(max_length=110)
    Mobile_2=models.CharField(max_length=110)
    Adresse=models.CharField(max_length=210)
    Wilaia=models.CharField(max_length=110)
    Commune=models.CharField(max_length=110)
    Note_Client=models.CharField(max_length=110)
    Numero_de_commande=models.CharField(max_length=110)
    nam_Produit=models.CharField(max_length=110)
    nober_Produit=models.CharField(max_length=110)
    type_livraison=models.CharField(max_length=110)
    prix_livraison=models.CharField(max_length=110)
    prix_Total_a_ramasser=models.CharField(max_length=110)
    

    id_commande=models.CharField(max_length=110)
    codebar_zrexpress=models.CharField(max_length=110)

    Appel=models.CharField(max_length=110)
    Préparation=models.CharField(max_length=110)
    Cours=models.CharField(max_length=110)

    prix_roter=models.CharField(max_length=110)

    def __str__(self):
        return str(self.user)           
    



















class statu(models.Model):
 
    status=models.CharField(max_length=110)
    icon=models.ImageField(upload_to='mediaa/slider_imgs')
   
    def __str__(self):
        return str(self.status)












#قسم خاص بإدخال الولايات
class namepack(models.Model):
    
    namepack=models.CharField(max_length=110)
    def __str__(self):
        return self.namepack 

class Livraison(models.Model):
  
 
    wilaia=models.CharField(max_length=110)
    prix_livraison_domicile=models.IntegerField(default=0)
    prix_livraison_desktop=models.IntegerField(default=0)
   

    def __str__(self):
        return str(self.wilaia)


class Liste_des_demandes(models.Model):
   # discount=(('ggggggg','gggggggggggggg'))
    
   
     nom_et_Prenom=models.CharField(max_length=110)


   
     phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$')
     phone_number = models.CharField(validators=[phone_regex], max_length=10)

     num1=models.CharField(max_length=11, blank=True ,null=True, default='0')
   # wilayaa=models.ForeignKey(Livraison, on_delete=models.CASCADE)
     wilayaa=models.ForeignKey(Livraison, on_delete=models.CASCADE)
    # wilayaa=models.ForeignKey(wilaya, on_delete=models.CASCADE)

    # wilayaa=models.CharField(max_length=110, blank=True)

     type_livraison=models.CharField(max_length=110, blank=True, null=True)
     prix_livraison=models.IntegerField(default=0, blank=True, null=True)
     prix_Total_a_ramasser=models.IntegerField(default=0, blank=True, null=True)
   # wilaya=models.CharField(max_length=110)
     ladresse_complete=models.CharField(max_length=150, null=True)
   
     numkamiya =models.IntegerField(default=1)
     product = models.CharField(max_length=110, blank=True)

   # product = models.ForeignKey(add_prodact , editable=False, on_delete=models.CASCADE)
   # nom = 'nom'
   # FAHRENHEIT = 'F' 
   # KELVIN = 'K'
   # TEMP_CHOICES = (
   # (nom_et_Prenom, 'nom'),
   # (FAHRENHEIT, 'Fahrenheit'),
   # (KELVIN, 'Kelvin')
    # )
   # temperature_scale = models.CharField(max_length=1,choices=TEMP_CHOICES, default=nom)
     color=models.CharField(max_length=250, blank=True )
   # Tail=models.ForeignKey(Tail_shoes, on_delete=models.CASCADE, blank=True, null=True)



    
     typepack=models.ForeignKey(namepack, on_delete=models.CASCADE, blank=True, null=True)
     name_prodact_achter=models.CharField(max_length=250, blank=True ,null=True)
     size=models.CharField(max_length=250, blank=True ,null=True)
     sizeclothing=models.CharField(max_length=250, blank=True )
     def __str__(self):
        return self.nom_et_Prenom 
    


     
#class Liste_des_commandes2(models.Model):
  
    
    # nom_et_Prenom=models.CharField(max_length=110)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$')
    # phone_number = models.CharField(validators=[phone_regex], max_length=10)
    # num1=models.CharField(max_length=11, blank=True ,null=True, default='0')
    # wilayaa=models.ForeignKey(Livraison, on_delete=models.CASCADE)
    # type_livraison=models.CharField(max_length=110, blank=True, null=True)
    # prix_livraison=models.IntegerField(default=0, blank=True, null=True)
    # prix_Total_a_ramasser=models.IntegerField(default=0, blank=True, null=True)
    # ladresse_complete=models.CharField(max_length=150, null=True)
    # numkamiya =models.IntegerField(default=1)
    # product = models.CharField(max_length=110, blank=True)
    # color=models.CharField(max_length=250, blank=True )
    # typepack=models.ForeignKey(namepack, on_delete=models.CASCADE, blank=True, null=True)
    #name_prodact_achter=models.CharField(max_length=250, blank=True ,null=True)
    # size=models.CharField(max_length=250, blank=True ,null=True)
    # sizeclothing=models.CharField(max_length=250, blank=True )


   


    # def __str__(self):
    #    return self.nom_et_Prenom 







from django.utils.timezone import now

class Liste_des_commandes(models.Model):
    nom_et_Prenom = models.CharField(max_length=110)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=10)
    num1 = models.CharField(max_length=11, blank=True, null=True, default='0')
    wilayaa = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    type_livraison = models.CharField(max_length=110, blank=True, null=True)
    prix_livraison = models.IntegerField(default=0, blank=True, null=True)
    prix_Total_a_ramasser = models.IntegerField(default=0, blank=True, null=True)
    ladresse_complete = models.CharField(max_length=150, null=True)
    numkamiya = models.IntegerField(default=1)
    product = models.CharField(max_length=110, blank=True)
    color = models.CharField(max_length=250, blank=True)
    typepack = models.ForeignKey(namepack, on_delete=models.CASCADE, blank=True, null=True)
    name_prodact_achter = models.CharField(max_length=250, blank=True, null=True)
    size = models.CharField(max_length=250, blank=True, null=True)
    sizeclothing = models.CharField(max_length=250, blank=True)


    date_commande = models.DateTimeField(default=now, blank=True, null=True)
    # **حقل جديد لتاريخ الطلب**
  #  date_commande = models.DateTimeField(auto_now_add=True)
    url_image = models.CharField(max_length=510, default="https://example.com/default-image.jpg" , blank=True, null=True)

    # **حالات الطلب بما فيها محاولات الاتصال بالزبون**
    STATUTS = [
        ('new', 'جديد'),
        ('pending', 'قيد التأكيد'),
        ('call_1', 'الاتصال مرة'),
        ('call_2', 'الاتصال مرتين'),
        ('call_3', 'الاتصال ثلاث مرات'),
        ('confirmed', 'مؤكدة'),
        ('delivery', 'شركة التوصيل'),
        ('completed', 'مكتملة'),
        ('all', 'الكل'),
        ('canceled', 'ملغي'),  # إضافة خيار "ملغي"
    ]
    
    statut_commande = models.CharField(max_length=20, choices=STATUTS, default='new')

    def get_statut_display_ar(self):
        """ دالة لإرجاع الحالة باللغة العربية للمستخدم """
        return dict(self.STATUTS).get(self.statut_commande, 'غير معروف')

    def __str__(self):
        return f"{self.nom_et_Prenom} - {self.get_statut_display_ar()}"



















class Liste_commandes(models.Model):
  
    
     nom_et_Prenom=models.CharField(max_length=110)
     phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$')
     phone_number = models.CharField(validators=[phone_regex], max_length=10)
     num1=models.CharField(max_length=11, blank=True ,null=True, default='0')
     wilayaa=models.ForeignKey(Livraison, on_delete=models.CASCADE)
     type_livraison=models.CharField(max_length=110, blank=True, null=True)
     prix_livraison=models.IntegerField(default=0, blank=True, null=True)
     prix_Total_a_ramasser=models.IntegerField(default=0, blank=True, null=True)
     ladresse_complete=models.CharField(max_length=150, null=True)
     numkamiya =models.IntegerField(default=1)
     product = models.CharField(max_length=110, blank=True)
     color=models.CharField(max_length=250, blank=True )
     typepack=models.ForeignKey(namepack, on_delete=models.CASCADE, blank=True, null=True)
     name_prodact_achter=models.CharField(max_length=250, blank=True ,null=True)
     size=models.CharField(max_length=250, blank=True ,null=True)
     sizeclothing=models.CharField(max_length=250, blank=True )



     date = models.DateTimeField(auto_now_add=True, blank=True)




     order_1 = 'A'
     order_2 = 'B' 
     order_3 = 'C'
     order_4 = 'D'     
     order_5 = 'E'
     order_6 = 'F' 


     ORDER = (
    
    
     (order_1, 'طلب جديد'),
     (order_2, 'لم يرد على الإتصال'),
     (order_3, ' مؤجلة'),
     (order_4, ' ملغي'),
     (order_5, 'مؤكدة'),
     (order_6, ' عند شركة التوصيل'),
    
      )
    


     order_status=models.CharField(max_length=1,choices=ORDER, default=order_1)












     def __str__(self):
        return self.nom_et_Prenom 











class Listecommandi(models.Model):
  
    
     nom_et_Prenom=models.CharField(max_length=110)
     phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$')
     phone_number = models.CharField(validators=[phone_regex], max_length=10)
     num1=models.CharField(max_length=11, blank=True ,null=True, default='0')
     wilayaa=models.ForeignKey(Livraison, on_delete=models.CASCADE)
     type_livraison=models.CharField(max_length=110, blank=True, null=True)
     prix_livraison=models.IntegerField(default=0, blank=True, null=True)
     prix_Total_a_ramasser=models.IntegerField(default=0, blank=True, null=True)
     ladresse_complete=models.CharField(max_length=150, null=True)
     numkamiya =models.IntegerField(default=1)
     product = models.CharField(max_length=110, blank=True)
     color=models.CharField(max_length=250, blank=True )
     typepack=models.ForeignKey(namepack, on_delete=models.CASCADE, blank=True, null=True)
     name_prodact_achter=models.CharField(max_length=250, blank=True ,null=True)
     size=models.CharField(max_length=250, blank=True ,null=True)
     sizeclothing=models.CharField(max_length=250, blank=True )






 
     TYP_1 = 'D'
     TYP_2 = 'A' 
    

     TEMP = (
    
    
     (TYP_1, 'توقيف'),
     (TYP_2, 'تفعيل'),
    
      )
    


     order_status=models.CharField(max_length=1,choices=TEMP, default=TYP_1)






     def __str__(self):
        return self.nom_et_Prenom 






















class add_prodact(models.Model):
   # discount=(('ggggggg','gggggggggggggg'))

    Product_title=models.CharField(max_length=100)
    #discountooooo=models.CharField(max_length=200)
    #discount_dea=models.CharField(choices=discount,max_length=100)
    prix=models.IntegerField()
    prix_old=models.IntegerField()
    
    Product_Description=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='media/slider_imgs')
    Image_2=models.ImageField(upload_to='media/slider_imgs')
    title_Image_2=models.CharField(max_length=100)
    text_Image_2=models.CharField(max_length=400)
    url_video_youtube=models.CharField(max_length=1000)
    Image_center=models.ImageField(upload_to='media/slider_imgs')
    Image_foter_1=models.ImageField(upload_to='media/slider_imgs')
    Image_foter_2=models.ImageField(upload_to='media/slider_imgs')
    Image_foter_3=models.ImageField(upload_to='media/slider_imgs')
    title_Image_foter=models.CharField(max_length=100)
    text_Image_foter=models.CharField(max_length=400)
    link=models.CharField(max_length=100)


    name_pixel=models.CharField(max_length=500, blank=True, null=True)
    num_pixel=models.CharField(max_length=500, blank=True, null=True)











   
   




   
   
    TYP_1 = 'D'
    TYP_2 = 'A' 
    

    TEMP = (
    
    
    (TYP_1, 'توقيف'),
    (TYP_2, 'تفعيل'),
    
     )
    


    active_color=models.CharField(max_length=1,choices=TEMP, default=TYP_1)
    active_tail=models.CharField(max_length=1,choices=TEMP, default=TYP_1)
    active_tailclothes=models.CharField(max_length=1,choices=TEMP, default=TYP_1)




    TYP_1 = 'A'
    TYP_2 = 'B' 
    TYP_3 = 'C'
    TYP_4 = 'D'
    TYP_5 = 'E'
    TYP_6 = 'F' 
    TYP_7 = 'G'
    TYP_8 = 'H'
    

    PART = (
    
    
    (TYP_1, 'القائمة _القسم الاول'),
    (TYP_2, 'القائمة_القسم الثاني'),
    (TYP_3, 'القائمة _القسم الثالث'),
    (TYP_4, 'القائمة_القسم الرابع'),
    (TYP_5, 'القائمة ا_القسم الخامس'),
    (TYP_6, 'القسم الثالث'),
    (TYP_7, 'القسم الرابع'),
    (TYP_8, 'القسم الخامس'),
     )

    partion=models.CharField(max_length=1,choices=PART, default=TYP_1)
   

    #tails=models.ForeignKey(tail, on_delete=models.CASCADE)
   
    #publications = models.ManyToManyField(Publication)






    tail1=models.CharField(max_length=3, blank=True)
    tail2=models.CharField(max_length=3, blank=True)
    tail3=models.CharField(max_length=3, blank=True)
    tail4=models.CharField(max_length=3, blank=True)
    tail5=models.CharField(max_length=3, blank=True)
    tail6=models.CharField(max_length=3, blank=True)
    tail7=models.CharField(max_length=3, blank=True)
    tail8=models.CharField(max_length=3, blank=True)
    tail9=models.CharField(max_length=3, blank=True)
    tail10=models.CharField(max_length=3, blank=True)
    tail11=models.CharField(max_length=3, blank=True)
    tail12=models.CharField(max_length=3, blank=True)
    tail13=models.CharField(max_length=3, blank=True)
    tail14=models.CharField(max_length=3, blank=True)
    tail15=models.CharField(max_length=3, blank=True)





    color1=models.CharField(max_length=11, blank=True)
    color2=models.CharField(max_length=11, blank=True)
    color3=models.CharField(max_length=11, blank=True)
    color4=models.CharField(max_length=11, blank=True)
    color5=models.CharField(max_length=11, blank=True)
    color6=models.CharField(max_length=11, blank=True)
    color7=models.CharField(max_length=11, blank=True)
    color8=models.CharField(max_length=11, blank=True)





    Tail_clothesr1=models.CharField(max_length=11, blank=True, null=True)
    Tail_clothes2=models.CharField(max_length=11, blank=True, null=True)
    Tail_clothes3=models.CharField(max_length=11, blank=True, null=True)
    Tail_clothes4=models.CharField(max_length=11, blank=True, null=True)
    Tail_clothes5=models.CharField(max_length=11, blank=True, null=True)
    Tail_clothes6=models.CharField(max_length=11, blank=True, null=True)
   

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # معالجة حجم الصور
        self.resize_image(self.Image, (800, 600))
        self.resize_image(self.Image_2, (800, 600))
        self.resize_image(self.Image_center,  (800, 600))
        self.resize_image(self.Image_foter_1, (800, 600))
        self.resize_image(self.Image_foter_2,  (800, 600))
        self.resize_image(self.Image_foter_3, (800, 600))

    def resize_image(self, image_field, max_size):
        if image_field and hasattr(image_field, 'path'):
            img = Image.open(image_field.path)
            if img.height > max_size[1] or img.width > max_size[0]:
                img.thumbnail(max_size, Image.LANCZOS)
                img.save(image_field.path, quality=85)





    def __str__(self):
        return self.Product_title         
    











class domainfb(models.Model):
    namemeta=models.CharField(max_length=200)
    codemeta=models.CharField(max_length=200)
    def __str__(self):
        return self.namemeta 
    
    
class menu(models.Model):
   
    partition_title_1=models.CharField(max_length=200)
    partition_title_2=models.CharField(max_length=200)
    partition_title_3=models.CharField(max_length=200)
    partition_title_4=models.CharField(max_length=200)
    partition_title_5=models.CharField(max_length=200)
    def __str__(self):
        return self. partition_title_1 
    


class coverwebsite(models.Model):
    Logo=models.ImageField(upload_to='mediaa/slider_imgs')
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class header(models.Model):
    Logo=models.ImageField(upload_to='media/slider_imgs')
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title        
    










class interfacewebsite(models.Model):
    Logo = models.ImageField(upload_to='media/slider_imgs', blank=True, null=True)
   
    title = models.CharField(max_length=200, blank=True, null=True)
    title_big = models.CharField(max_length=200, blank=True, null=True)
    title_small = models.CharField(max_length=200, blank=True, null=True)
    cover = models.ImageField(upload_to='media/slider_imgs', blank=True, null=True)
    menu1 = models.CharField(max_length=200, blank=True, null=True)
    menu2 = models.CharField(max_length=200, blank=True, null=True)
    menu3 = models.CharField(max_length=200, blank=True, null=True)
    menu4 = models.CharField(max_length=200, blank=True, null=True)
    menu5 = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    pantirst = models.CharField(max_length=200, blank=True, null=True)
    linkid = models.CharField(max_length=200, blank=True, null=True)
    num_phone= models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
       # return self.title   

        if self.title:
            return self.title
        else:
            return f"InterfaceWebsite {self.pk}"











class pixlfb(models.Model):
    namepixel=models.CharField(max_length=200)
    idpixel=models.CharField(max_length=200)
    def __str__(self):
        return self.namepixel 






#قسم خاص بإدخال الولايات
class wilaya(models.Model):
    wilaya=models.CharField(max_length=110)
    def __str__(self):
        return self.wilaya 
    
    
#header add logo and title
class follow(models.Model):
    facebook=models.CharField(max_length=200)
    instagram=models.CharField(max_length=200)
    def __str__(self):
        return self.title
    


class Liste_storecharging(models.Model):
   # discount=(('ggggggg','gggggggggggggg'))
    
   
    nom_et_Prenom=models.CharField(max_length=110)
    num1=models.CharField(max_length=11)
    wilayaa=models.ForeignKey(wilaya, on_delete=models.CASCADE)
   # wilaya=models.CharField(max_length=110)
    ladresse_complete=models.CharField(max_length=150, null=True)
   
 

    TYP_1 = 'A'
    TYP_2 = 'B' 
    TYP_3 = 'C'
    TYP_4 = 'D'
    TYP_5 = 'E'
    TYP_6 = 'F' 
    TYP_7 = 'G'
    TYP_8 = 'H'
    

    PART = (
    
    
    (TYP_1, '  3000 DA '),
    (TYP_2, ' 6000 DA '),
    (TYP_3, ' 9000 DA '),
    (TYP_4, ' 12000 DA '),
    (TYP_5, '  20000 DA '),
    (TYP_6, ' 30000 DA '),
    (TYP_7, ' 60000 DA'),
   
     )

    offer=models.CharField(max_length=1,choices=PART, default=TYP_1)


   
    def __str__(self):
        return self.nom_et_Prenom 










class video(models.Model):
    titel_video= models.CharField(max_length=500, blank=True, null=True)
    url_video= models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.titel_video   