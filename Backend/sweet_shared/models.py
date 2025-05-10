# Create your models here.
from django.db import models
from django.contrib.auth.models import User




from django.contrib import admin




class SweetType(models.Model):

    name = models.CharField(max_length=100,blank=True, null=True)
    username = models.CharField(max_length=120,blank=True, null=True)
    password= models.CharField(max_length=120,blank=True, null=True)


   

    email= models.CharField(max_length=120,blank=True, null=True )
    domainname = models.CharField(max_length=120,blank=True, null=True)
    wilaya = models.CharField(max_length=120,blank=True, null=True)
    address = models.CharField(max_length=120,blank=True, null=True)
    phonenumber= models.CharField(max_length=120,blank=True, null=True)
   





class confirmserial(models.Model):
   
    username = models.CharField(max_length=120, null=True, blank=True)
    serial = models.CharField(max_length=120, null=True, blank=True)
    confirmserial= models.CharField(max_length=120, null=True, blank=True)



class Typesofsubscriptionplan(models.Model):
   
    planname = models.CharField(max_length=120, null=True, blank=True)
    planprice = models.CharField(max_length=120, null=True, blank=True)
    advantage1= models.CharField(max_length=120, null=True, blank=True)  
    advantage2= models.CharField(max_length=120, null=True, blank=True)  
    advantage3= models.CharField(max_length=120, null=True, blank=True)  
    advantage4= models.CharField(max_length=120, null=True, blank=True)  
    advantage5= models.CharField(max_length=120, null=True, blank=True)  
    advantage6= models.CharField(max_length=120, null=True, blank=True)  
    advantage7= models.CharField(max_length=120, null=True, blank=True)  
    advantage8= models.CharField(max_length=120, null=True, blank=True)  
    advantage9= models.CharField(max_length=120, null=True, blank=True)  
    advantage10= models.CharField(max_length=120, null=True, blank=True)    



   
class bankinformation(models.Model):
   
    bankname = models.CharField(max_length=120, null=True, blank=True)
    nameandsurname= models.CharField(max_length=120, null=True, blank=True)
    accountnumber= models.CharField(max_length=120, null=True, blank=True)
    address= models.CharField(max_length=120, null=True, blank=True)
    email= models.CharField(max_length=120, null=True, blank=True)
    logobank= models.ImageField(upload_to='media/slider_imgs')

    def __str__(self):
        return self.bankname



class price(models.Model):
 
    order_price= models.CharField(max_length=20, null=True, blank=True)
    advanced_package= models.CharField(max_length=20, null=True, blank=True)
    legendary_package= models.CharField(max_length=20, null=True, blank=True)



class addpayments(models.Model):
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=120, null=True, blank=True)
    numberpayments = models.IntegerField(default=300)
    numbercemande = models.IntegerField(default=30)


    def __str__(self):
        return self.username





class add_payments(models.Model):
 
    username = models.CharField(max_length=120, null=True, blank=True)
    numbercemande = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="عدد الطلبيات")
    
    PACKAGE_CHOICES = [
        ('free', 'الباقة المجانية'),
        ('advanced', 'الباقة المتطورة'),
        ('legendary', 'الباقة الأسطورية'),
    ]

    package = models.CharField(max_length=50, choices=PACKAGE_CHOICES, verbose_name="الباقة", null=True, blank=True)
    payment_type = models.CharField(max_length=500, verbose_name="نوع الدفع", null=True, blank=True)


  # جعل payment_type كـ ForeignKey يعتمد على bankname
    payment_type = models.ForeignKey( bankinformation, on_delete=models.SET_NULL, verbose_name="نوع الدفع", null=True, blank=True, related_name="payment_types_add" )





    
    upload_receipt = models.FileField(upload_to="receipts/", verbose_name="رفع الوصل", null=True, blank=True)
    start_date = models.DateField(verbose_name="تاريخ البداية", null=True, blank=True)
    end_date = models.DateField(verbose_name="تاريخ النهاية", null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ", null=True, blank=True)



    STATUS_CHOICES = [
     ('pending', 'قيد مراجعة'),
     ('active', 'نشطة'),
     ('completed', 'مكتملة'),
     ('rejected', 'رفض'),
    ]

    status = models.CharField(max_length=50,choices=STATUS_CHOICES,verbose_name="الحالة",null=True,blank=True)

    def __str__(self):
        return self.username if self.username else "No Username"



























class Payments(models.Model):
   
    username = models.CharField(max_length=120, null=True, blank=True)
    numberoforders = models.IntegerField(default=1)
    orderprice = models.CharField(max_length=120, null=True, blank=True)
    paymenttype = models.ForeignKey(bankinformation, on_delete=models.CASCADE)
  
    image = models.ImageField(upload_to='media/slider_imgs')

    TYP_1 = 'D'
    TYP_2 = 'A' 
    TEMP = ((TYP_1, 'قيد المراجعة'),(TYP_2, 'تاكيد'),)
    demand = models.CharField(max_length=1,choices=TEMP, default=TYP_1, null=True, blank=True )


    remainingprice = models.CharField(max_length=120, null=True, blank=True)



    TY_1 = 'D'
    TY_2 = 'A' 
    TEM = ((TYP_1, ' no gift'),(TYP_2, 'gift'),)
    gift = models.CharField(max_length=1,choices=TEM, default=TY_1, null=True, blank=True )



    







    
    
      
#قسم خاص بإدخال الولايات
class wilayaa(models.Model):
    wilaya=models.CharField(max_length=110)
    prixdomicile= models.IntegerField()
    prixstopdesk= models.IntegerField()

    def __str__(self):
        return self.wilaya 



 
    
    

class coliinformation(models.Model):
  
    nomcomplet  = models.CharField(max_length=120, null=True, blank=True)
    mobile1=models.CharField(max_length=12, null=True, blank=True)
    mobile2=models.CharField(max_length=12, null=True, blank=True)
    adresse=models.CharField(max_length=120, null=True, blank=True)

   
    wilaya = models.ForeignKey(wilayaa, on_delete=models.CASCADE)
 

    commune=models.CharField(max_length=120, null=True, blank=True)
    noteclient=models.CharField(max_length=120, null=True, blank=True)
    numerodecommande=models.CharField(max_length=120, null=True, blank=True)
    nameroduct=models.CharField(max_length=120, null=True, blank=True)






    TYP_1 = 'S'
    TYP_2 = 'I' 
    
    TEMP = (
    
    (TYP_1, 'FALSE'),
    (TYP_2, 'TRUE'),
    
     )    

    echange=models.CharField(max_length=1,choices=TEMP, default=TYP_1)


    TY_1 = 'DOMICEL'
    TY_2 = 'STOPDESK' 
    
    TEMP = (
    
    (TY_1, 'DOMICEL'),
    (TY_2, 'STOPDESK'),
    
     )    

    livrioncoli=models.CharField(max_length=8,choices=TEMP, default=TY_1)
    prixproduct = models.IntegerField(default=1, null=True, blank=True)
    prixretour = models.CharField(max_length=50, null=True, blank=True)
  


    tracking=models.CharField(max_length=120, null=True, blank=True)
    Date=models.CharField(max_length=120, null=True, blank=True)
    bureauactuel=models.CharField(max_length=120, null=True, blank=True)
    numeroreclamation=models.CharField(max_length=120, null=True, blank=True)
    situationcoli=models.CharField(max_length=120, null=True, blank=True)




    username  = models.CharField(max_length=120, null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.nomcomplet    
    





class Situation(models.Model):
     situation = models.CharField(max_length=120, null=True, blank=True)

     def __str__(self):
        return self.situation






class SituationColis(models.Model):
    tracking = models.CharField(max_length=120, null=True, blank=True)
    situations = models.ManyToManyField(Situation)

    def __str__(self):
        return self.tracking

    class Meta:
        verbose_name_plural = "حالات الشحن" 
 









class Confirmerlidentite(models.Model):

   username= models.CharField(max_length=120, null=True, blank=True)
   nom= models.CharField(max_length=120, null=True, blank=True)
   Prenom= models.CharField(max_length=120, null=True, blank=True)
   imagecard= models.ImageField(upload_to='media/slider_imgs')
   imageegister= models.ImageField(upload_to='media/slider_imgs', null=True, blank=True)



   TYP_1 = 'FALSE'
   TYP_2 = 'TRUE' 
    
   TEMP = (
    
   (TYP_1, 'FALSE'),
   (TYP_2, 'TRUE'),
    
   )  
   confirmer=models.CharField(max_length=5,choices=TEMP, default=TYP_1, null=True, blank=True)


   def __str__(self):
        return self.username    
     







    
    





class domainn(models.Model):
    domainee = models.CharField(max_length=200)
    usernamee = models.CharField(max_length=120, null=True, blank=True)

    TYP_1 = 'FALSE'
    TYP_2 = 'TRUE' 

    TEMP = (
        (TYP_1, 'FALSE'),
        (TYP_2, 'TRUE'),
    )  
    confirmerdoman = models.CharField(max_length=5, choices=TEMP, default=TYP_1, null=True, blank=True)
    
    def __str__(self):
        return self.usernamee or f"Domainn {self.pk}"  # إذا كان usernamee هو None، استخدم اسم افتراضي





#قسم خاص بإدخال الولايات
class sahlaboost(models.Model):
    name_desktop=models.CharField(max_length=310, null=True, blank=True)
    serial=models.CharField(max_length=310, null=True, blank=True)
    conferm_serial=models.CharField(max_length=310, null=True, blank=True)

    username= models.CharField(max_length=120, null=True, blank=True)
    nom= models.CharField(max_length=120, null=True, blank=True)
    Prenom= models.CharField(max_length=120, null=True, blank=True)
    num_phone= models.CharField(max_length=120, null=True, blank=True)
    def __str__(self):
        return self.username 









#قسم خاص بإدخال الولايات
class activation_money_book(models.Model):
   
    serial=models.CharField(max_length=310, null=True, blank=True)
    conferm_serial=models.CharField(max_length=310, null=True, blank=True)
    username= models.CharField(max_length=120, null=True, blank=True)
    nom= models.CharField(max_length=120, null=True, blank=True)
    Prenom= models.CharField(max_length=120, null=True, blank=True)
    num_phone= models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.username if self.username else "Unknown Username"
    






class video_formation(models.Model):
    titel_video= models.CharField(max_length=500, blank=True, null=True)
    url_video= models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.titel_video   






class Link_chromedriver(models.Model):
    name_url = models.CharField(max_length=500, blank=True, null=True)
    download_path_chromedriver = models.CharField(max_length=1500, blank=True, null=True)
    video_url = models.CharField(max_length=1000, blank=True, null=True)  # حقل رابط الفيديو
    desktop_file_path = models.CharField(max_length=1500, blank=True, null=True)  # حقل رابط الملف على سطح المكتب

    def __str__(self):
        return self.name_url     
    










