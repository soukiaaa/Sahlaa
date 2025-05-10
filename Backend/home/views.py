from django.shortcuts import render
from profiles.models import Profile,Commandes,Liste_des_demandes,Liste_des_commandes,add_prodact,header,coverwebsite,menu,domainfb,pixlfb,Liste_storecharging,follow,interfacewebsite,Livraison
from django.contrib.auth.models import User
from profiles.forms import Addproduct,Listeorders,PaymentForm,CustomerForm,Livraisonform, CreateTenantForm,LoginForm,SweetTypeForm,ActivationForm
from django.shortcuts import render, redirect,get_object_or_404

from profiles.forms import OpenStore,OpenStoreForm,sahlaboostForm,CreateTenantSuperuserForm,ConfirmSerialForm,PixlfbForm,Storecharging,interfacewebsiteForm,YourDomainForm,Livraisonform
from client.models import Client, Domain
from sweet_shared.models import confirmserial,SweetType,domainn,addpayments,video_formation

from urllib.parse import urlparse
from django.core.paginator import Paginator

from sweet_shared.models import activation_money_book,SweetType,Typesofsubscriptionplan,bankinformation,price,Payments,Confirmerlidentite,add_payments

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django_tenants.utils import schema_context
from django.contrib.auth.models import User
from .serializers import *


from django.shortcuts import render, redirect












from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index_vieww(request):


 # استخراج النطاق الفرعي من الطلب
 host = request.get_host()
 subdomain = host.split('.')[0] if '.' in host else None  # استخراج النطاق الفرعي إذا كان موجودًا




 if host == '127.0.0.1:8000':
        # إذا كان العنوان هو localhost، فأعرض صفحة home.html
        return render(request, 'home/home.html')


 if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the username and password exist in the database
            try:
                user = SweetType.objects.get(username=username, password=password)
                # Redirect to the URL containing domainname
                return redirect(f'http://{user.domainname}.localhost:8000/')
                #return redirect(f'https://{user.domainname}.sahladz.com/')
            
            except SweetType.DoesNotExist:
                # If username and password don't exist, render the login page with an error message
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials. Please try again.'})
 else:
        form = LoginForm()  # Initialize an empty form







 if subdomain is not None:
    # التحقق من وجود النطاق الفرعي في قاعدة البيانات
    try:
        client = Client.objects.get(schema_name=subdomain)
    except Client.DoesNotExist:
        # إذا لم يكن النطاق الفرعي موجودًا، فأعرض صفحة 404
        return render(request, '404.html', status=404)

    # التبديل إلى مخطط المستأجر
    with schema_context(client.schema_name):
        try:
            profile = Profile.objects.get(user=request.user)
        except Exception as e:
            profile = None
            print('Exception:', e)













 

    interface = interfacewebsite.objects.all()

    domains = domainfb.objects.all()  # استرجاع جميع السجلات من نموذج domainfb
    partitionname = menu.objects.all()


  

 
   


    hea = coverwebsite.objects.all()
    head = header.objects.all()
   
    prodact = add_prodact.objects.all()
   

    #print(prodact)
    print('partitionnam',partitionname)
   



    print('imagessscove',hea)
  
    print('uuuuuuuuuuuu',head)
   
    print('prooooooooooooooooooooooooooo',prodact)
   
    context ={
             
              'interface':interface,
              'prodact':prodact,
              'head':head,
              'hea':hea,
              'partitionname':partitionname,
              'domains': domains,

               'profile': profile,
          
               

    }



    return render(request, 'home/index.html',context)
 





def index_view(request):
    host = request.get_host()
    subdomain = host.split('.')[0] if '.' in host else None

    if host == '127.0.0.1:8000':
        form = LoginForm()  # إنشاء نموذج LoginForm بدلاً من SweetTypeForm
        if request.method == 'POST':
            form = LoginForm(request.POST)  # استخدام LoginForm بدلاً من SweetTypeForm
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                try:
                    user = SweetType.objects.get(username=username, password=password)
                  
                    return redirect(f'http://{user.domainname}.localhost:8000/')
                    #return redirect(f'https://{user.domainname}.sahladz.com/')
                except SweetType.DoesNotExist:
                    return render(request, 'home/home.html', {'form': form, 'error': 'Invalid credentials. Please try again.'})
        
        # عرض النموذج في حالة GET أو POST غير صالح
        return render(request, 'home/home.html', {'form': form})







    if subdomain is not None:
        try:
            client = Client.objects.get(schema_name=subdomain)
        except Client.DoesNotExist:
            return render(request, '404.html', status=404)

        with schema_context(client.schema_name):
            try:
                profile = Profile.objects.get(user=request.user)
            except Exception as e:
                profile = None
                print('Exception:', e)

            interface = interfacewebsite.objects.all()
            domains = domainfb.objects.all()
            partitionname = menu.objects.all()
            hea = coverwebsite.objects.all()
            head = header.objects.all()
            prodact = add_prodact.objects.all()

            context = {
                'form': LoginForm(),  # إنشاء نموذج LoginForm بدلاً من SweetTypeForm
                'interface': interface,
                'prodact': prodact,
                'head': head,
                'hea': hea,
                'partitionname': partitionname,
                'domains': domains,
                'profile': profile,
            }

            return render(request, 'home/index.html', context)

    return render(request, 'login.html', {'form': LoginForm()})  # إنشاء نموذج LoginForm بدلاً من SweetTypeForm



#def command(request):

  #  try:
       
     #   proe = commandes.objects.get(user=request.user)
       
      
        
   # except Exception as e:
        
   #     proe = None
  #      print('Exception : ', e)

  #  context = {
   #     'proe': proe,
   # }
   # print('Exception 888888888888888888888888888888888: ', context)
   # return render(request, 'commandes.html',context)


def command(request):

    try:
        
        proe = Commandes.objects.all()
      #  proe = Commandes.objects.get(Nom_Complet="bboy")
      
        
    except Exception as e:
        
        proe = None
        print('Exception : ', e)

   # context = {'proe': proe.filter(Nom_Complet="bboy")}
    context = {'proe': proe.filter(user=request.user)}
     #context = {'proe': proe,}
    print('Exception 888888888888888888888888888888888: ', context)
    return render(request, 'commandes.html',context)







def d (request):


    return render(request, 'd.html')













def dashboard01(request):








    context = {}  # تأكد من أن context معرف دائمًا


    from profiles.populate_wilayas import populate_wilayas
                  # استدعاء الدالة لتعبئة البيانات بعد تسجيل الدخول بنجاح
    populate_wilayas()










    if request.user.is_authenticated:






    # استخراج النطاق الفرعي من الطلب
        host = request.get_host()

        subdomain = host.split('.')[0] if '.' in host else None  # استخراج النطاق الفرعي إذا كان موجودًا
        print("subdomain:",subdomain)
        sub=subdomain+'.localhost'
        #sub=subdomain+'.sahladz.com'

        username = None
        if subdomain is not None:
            try:
            # البحث في الجدول باستخدام subdomain في خانة domainname
             sweet_type = SweetType.objects.filter(domainname=sub).first()
            # استرجاع username التابع له
             if sweet_type is not None:
                    # استرجاع username التابع له
                    username = sweet_type.username
                    print('username:', username)
             else:
                    print("Error: sweet_type is None for subdomain:", sub)

            except SweetType.DoesNotExist:
            # التعامل مع الحالة التي لا يوجد فيها تطابق
               username = None


   
        current_user = request.user  # الحصول على المستخدم الحالي

        
        # الحصول على جميع المدفوعات للمستخدم الحالي بناءً على اسم المستخدم
        payments = addpayments.objects.filter(username=username)
      
        if payments.exists():
            print('sssssss')
            # إذا كانت هناك مدفوعات متعددة، التعامل معها (مثلاً، أخذ أول واحدة)
            payment = payments.first()
            created = False
        else:
            print('fffffff')
            # إذا لم تكن هناك مدفوعات، إنشاء واحدة جديدة بناءً على اسم المستخدم
            payment = addpayments.objects.create(
                user=current_user,
                username=username,
                numberpayments=300,
                numbercemande=30
            )
            created = True

        payments_total = payments  # حفظ جميع المدفوعات التي تم الحصول عليها
        prodact_total = add_prodact.objects.all().count()
        Liste_demandest = Liste_des_commandes.objects.all().count()










   # استخراج اسم المستخدم الحالي
        current_username = request.user.username

    # الحصول على سجلات الدفع الخاصة بالمستخدم الحالي فقط
        payments = add_payments.objects.filter(username=current_username)

 # التحقق من وجود دفع نشط
        active_payment = payments.filter(status="active").first()

    # تحديث الحالة إذا كانت الباقة قد انتهت
        if active_payment and active_payment.end_date:
            current_date = datetime.now().date()  # التاريخ الحالي
            if active_payment.end_date < current_date:
            # إذا انتهى تاريخ الباقة، تحديث الحالة إلى "completed"
                active_payment.status = "completed"
                active_payment.save()
                active_payment = None  # إعادة ضبط الباقة النشطة إلى None




        if active_payment:
            if active_payment.package == "free":
                   # الباقة المجانية - عرض عدد الطلبيات المتبقية
                   context['active_payment'] = {
                       'type': 'free',
                       'remaining_orders': active_payment.numbercemande,
                   }
            elif active_payment.package in ["advanced", "legendary"]:
                # الباقة المتطورة أو الأسطورية - عرض تاريخ النهاية

                context['active_payment'] = {
                    'type': active_payment.package,
                    'end_date': active_payment.end_date,
                }
        else:
        # لا توجد باقة نشطة
            pass



















     
        context = {
            'Liste_demandest': Liste_demandest,
            'prodact_total': prodact_total,
            'payments_total': payments_total,

            'payments': payments,  # جميع السجلات للمستخدم الحالي
            'active_payment': None,
            'message': None,
            'error': None,


        }

        return render(request, 'dashbord/dashbord.html', context)
    else:
        # إعادة توجيه المستخدم إلى صفحة تسجيل الدخول
        return redirect('login_view')  # يجب استبدال 'login_view' باسم الرابط الخاص بصفحة تسجيل الدخول في مشروعك







from profiles.populate_wilayas import populate_wilayas

def dashboard(request):
    """
    عرض لوحة التحكم الخاصة بالمستخدم بعد تسجيل الدخول بنجاح.
    """

    if not request.user.is_authenticated:
        return redirect('login_view')  # إعادة التوجيه لصفحة تسجيل الدخول إذا لم يكن المستخدم مسجلاً للدخول

    # تعبئة بيانات الولايات عند الدخول للوحة التحكم
    populate_wilayas()

    # استخراج النطاق الفرعي من الطلب
    host = request.get_host()
    subdomain = host.split('.')[0] if '.' in host else None
    print("subdomain:", subdomain)

    sub = f"{subdomain}.localhost"  # يمكنك تغييرها لـ "sahladz.com" عند النشر

    # محاولة جلب اسم المستخدم المرتبط بالنطاق الفرعي
    username = None
    if subdomain:
        sweet_type = SweetType.objects.filter(domainname=sub).first()
        if sweet_type:
            username = sweet_type.username
            print('username:', username)

    current_user = request.user  # المستخدم الحالي

    # جلب جميع المدفوعات للمستخدم الحالي
    payments = addpayments.objects.filter(username=username)

    if payments.exists():
        payment = payments.first()  # أخذ أول دفعة إذا وُجدت
        created = False
    else:
        # إنشاء دفعة جديدة إذا لم تكن هناك مدفوعات سابقة
        payment = addpayments.objects.create(
            user=current_user,
            username=username,
            numberpayments=300,
            numbercemande=30
        )
        created = True

    # حساب عدد المنتجات وعدد الطلبات الإجمالية
    prodact_total = add_prodact.objects.count()
    Liste_demandest = Liste_des_commandes.objects.count()

    # استخراج اسم المستخدم الحالي واستدعاء الدالة الخاصة بحالة الاشتراك
    current_username = request.user.username
    active_payment_status, payments = get_active_payment_status(current_username)

    # إعداد السياق لتمريره إلى القالب
    context = {
        'Liste_demandest': Liste_demandest,
        'prodact_total': prodact_total,
        'payments_total': payments,
        'payments': payments,
        'active_payment': active_payment_status,  # معلومات الباقة النشطة
        'message': None,
        'error': None,
    }

    return render(request, 'dashbord/dashbord.html', context)


import socket
from django.shortcuts import render



def formation(request):
    current_user = request.user  # الحصول على المستخدم الحالي
    
    # تعريف 'user_activation' كمتحول فارغ
    user_activation = None
    activate_status = 'not activate'  # حالة التفعيل الافتراضية    
    
    # التحقق من حالة التفعيل للمستخدم الحالي
    try:
        user_activation = activation_money_book.objects.get(username=current_user.username)
        activate_status = 'activate' if user_activation.serial == user_activation.conferm_serial else 'not activate'
    except activation_money_book.DoesNotExist:
        user_activation = None
        activate_status = 'not activate'

    # إذا كانت طريقة الطلب POST، معالجة النموذج
    if request.method == 'POST':
        form = ActivationForm(request.POST)  # تعبئة النموذج مع البيانات
        if form.is_valid():
            conferm_serial = form.cleaned_data.get('conferm_serial')

            # البحث عن السجل المطابق في قاعدة البيانات باستخدام serial
            try:
                user_activation = activation_money_book.objects.get(serial=conferm_serial)
                
                # إذا تم العثور على السجل، قم بتحديث conferm_serial و username
                user_activation.conferm_serial = conferm_serial
                user_activation.username = current_user.username  # تحديث اسم المستخدم الحالي
                user_activation.save()

                # تعيين حالة التفعيل
                if user_activation.serial == user_activation.conferm_serial:
                    activate_status = 'activate'
                else:
                    activate_status = 'not activate'
            except activation_money_book.DoesNotExist:
                # في حالة لم يتم العثور على السجل، قم بإبلاغ المستخدم بأن الكود غير صالح
                activate_status = 'invalid code'
                print("Invalid code: conferm_serial not found.")
    else:
        form = ActivationForm()  # عرض النموذج الفارغ


    # باقي الكود

    print('hostname:', socket.gethostname())

    from profiles.populate_wilayas import populate_wilayas
    populate_wilayas()



    # جلب قائمة الفيديوهات من قاعدة البيانات
    videos = video_formation.objects.all()








    if request.user.is_authenticated:
        # استخراج النطاق الفرعي من الطلب
        host = request.get_host()
        subdomain = host.split('.')[0] if '.' in host else None  # استخراج النطاق الفرعي إذا كان موجودًا
        sub = subdomain + '.localhost'  # تعديل النطاق

        username = None
        if subdomain is not None:
            try:
                sweet_type = SweetType.objects.filter(domainname=sub).first()
                if sweet_type is not None:
                    username = sweet_type.username
                else:
                    print("Error: sweet_type is None for subdomain:", sub)
            except SweetType.DoesNotExist:
                username = None

        payments = addpayments.objects.filter(username=username)
        if payments.exists():
            payment = payments.first()
            created = False
        else:
            payment = addpayments.objects.create(
                user=current_user,
                username=username,
                numberpayments=300,
                numbercemande=30
            )
            created = True

        payments_total = payments
        prodact_total = add_prodact.objects.all().count()
        Liste_demandest = Liste_des_commandes.objects.all().count()

        context = {
            'Liste_demandest': Liste_demandest,
            'prodact_total': prodact_total,
            'payments_total': payments_total,
            'activate_status': activate_status,
            'form': form,
             'videos': videos , 
        }

        return render(request, 'formation.html', context)
    else:
        return redirect('login_view')






def formationn(request):


    current_user = request.user  # الحصول على المستخدم الحالي
    
    # تعريف 'user_activation' كمتحول فارغ
    user_activation = None
    activate_status = 'not activate'  # حالة التفعيل الافتراضية    
        # التحقق من حالة التفعيل للمستخدم الحالي
    try:
            user_activation = activation_money_book.objects.get(username=current_user.username)
            activate_status = 'activate' if user_activation.serial == user_activation.conferm_serial else 'not activate'
    except  activation_money_book.DoesNotExist:
            activate_status = 'not activate'











      # إذا كانت طريقة الطلب POST، معالجة النموذج
    if request.method == 'POST':
        form = ActivationForm(request.POST)  # تعبئة النموذج مع البيانات
        if form.is_valid():
            # حفظ conferm_serial في قاعدة البيانات
            conferm_serial = form.cleaned_data.get('conferm_serial')
            user_activation.conferm_serial = conferm_serial
            user_activation.save()
            # التحقق مرة أخرى من حالة التفعيل بعد الحفظ
            if user_activation.serial == user_activation.conferm_serial:
                activate_status = 'activate'
            else:
                activate_status = 'not activate'
    else:
        form = ActivationForm()  # عرض النموذج الفارغ














    print('hostnammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmme')

    hostname = socket.gethostname()
    print('hostname',hostname)

    from profiles.populate_wilayas import populate_wilayas
                  # استدعاء الدالة لتعبئة البيانات بعد تسجيل الدخول بنجاح
    populate_wilayas()










    if request.user.is_authenticated:






    # استخراج النطاق الفرعي من الطلب
        host = request.get_host()

        subdomain = host.split('.')[0] if '.' in host else None  # استخراج النطاق الفرعي إذا كان موجودًا
        print("subdomain:",subdomain)
        sub=subdomain+'.localhost'
        #sub=subdomain+'.sahladz.com'

        username = None
        if subdomain is not None:
            try:
            # البحث في الجدول باستخدام subdomain في خانة domainname
             sweet_type = SweetType.objects.filter(domainname=sub).first()
            # استرجاع username التابع له
             if sweet_type is not None:
                    # استرجاع username التابع له
                    username = sweet_type.username
                    print('username:', username)
             else:
                    print("Error: sweet_type is None for subdomain:", sub)

            except SweetType.DoesNotExist:
            # التعامل مع الحالة التي لا يوجد فيها تطابق
               username = None


   
        current_user = request.user  # الحصول على المستخدم الحالي

        
        # الحصول على جميع المدفوعات للمستخدم الحالي بناءً على اسم المستخدم
        payments = addpayments.objects.filter(username=username)
      
        if payments.exists():
            print('sssssss')
            # إذا كانت هناك مدفوعات متعددة، التعامل معها (مثلاً، أخذ أول واحدة)
            payment = payments.first()
            created = False
        else:
            print('fffffff')
            # إذا لم تكن هناك مدفوعات، إنشاء واحدة جديدة بناءً على اسم المستخدم
            payment = addpayments.objects.create(
                user=current_user,
                username=username,
                numberpayments=300,
                numbercemande=30
            )
            created = True

        payments_total = payments  # حفظ جميع المدفوعات التي تم الحصول عليها
        prodact_total = add_prodact.objects.all().count()
        Liste_demandest = Liste_des_commandes.objects.all().count()
     
        context = {
            'Liste_demandest': Liste_demandest,
            'prodact_total': prodact_total,
            'payments_total': payments_total,
            'activate_status': activate_status,
            'form': form  # تمرير النموذج إلى القالب

        }

        return render(request, 'formation.html', context)
    else:
        # إعادة توجيه المستخدم إلى صفحة تسجيل الدخول
        return redirect('login_view')  # يجب استبدال 'login_view' باسم الرابط الخاص بصفحة تسجيل الدخول في مشروعك




































def addaproduct(request):

 form = Addproduct()
 context ={
      
       "form":form,  
    }

 if request.method == 'POST':
   form = Addproduct(request.POST,request.FILES)
   print('form',form)
 
   if form.is_valid():
     
     form.save()
     print('444444444444444444444444444444444444444444')
     return redirect('/products/') 
 

 return render(request,'addproduct/addproduct.html',context)




























def delete_product(request, my_id):
	queryset = add_prodact.objects.get(id=my_id)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/products/')
	return render(request, 'delete_product.html')








def update_product(request, my_id):
    queryset = add_prodact.objects.get(id=my_id)
    form = Addproduct(instance=queryset)
    
    if request.method == 'POST':
        form = Addproduct(request.POST, request.FILES, instance=queryset)  # تأكيد إضافة request.FILES هنا
        if form.is_valid():
            form.save()
            return redirect('/products/')              
    
    context = {
        'pro': get_object_or_404(add_prodact, pk=my_id),  
        'form': form,
    }
    return render(request, 'addproduct.html', context)






def update_pixel_product(request, my_id):
    queryset = add_prodact.objects.get(id=my_id)
    form = Addproduct(instance=queryset)
    
    if request.method == 'POST':
        form = Addproduct(request.POST, request.FILES, instance=queryset)  # تأكيد إضافة request.FILES هنا
        if form.is_valid():
            form.save()
            return redirect('/products/')              
    
    context = {
        'pro': get_object_or_404(add_prodact, pk=my_id),  
        'form': form,
    }
    return render(request, 'addpixlproduct/addpixlproduct.html', context)

























def openstore(request):
    if request.method == 'POST':
        form = OpenStoreForm(request.POST)
        if form.is_valid():
            form.save()
            # قم بتنفيذ أي إجراء إضافي هنا بعد حفظ البيانات
            return render(request, 'success.html')  # قم بتحويل المستخدم إلى صفحة النجاح
    else:
        form = OpenStoreForm()
    return render(request, 'openstor.html', {'form': form})







#def inscription(request):
#    if request.method == 'POST':
#        form = OpenStore(request.POST)
#        if form.is_valid():
#            name = form.cleaned_data['name']
#            domain = form.cleaned_data['domain']
            
            # التحقق مما إذا كان الاسم مسجل مسبقًا
#            if name and Client.objects.filter(name=name).exists():
#                form.add_error('name', 'الإسم الذي ادخلته موجود من قبل يرجى تغييره')

            # التحقق مما إذا كان النطاق مسجل مسبقًا
#            elif domain and Domain.objects.filter(domain=domain).exists():
#                form.add_error('domain', 'النطاق الذي ادخلته موجود من قبل يرجى تغييره')

#            else:
                # قم بإنشاء مستخدم جديد وتخزينه في قاعدة البيانات
#                user = User.objects.create(username=name)  # يمكنك استخدام اسم المستخدم كاسم المستخدم الجديد
#                user.set_password('password_here')  # قم بتعيين كلمة مرور المستخدم الجديد
#                user.save()

                # قم بإنشاء مؤجر جديد (Tenant) وربطه بالمستخدم
#                form.save()

                # قم بتنفيذ أي إجراء إضافي هنا بعد حفظ البيانات
#                return redirect('success')  # قم بتحويل المستخدم إلى صفحة النجاح
#    else:
#        form = OpenStore()
    
#    return render(request, 'inscription.html')







from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
import re











def inscriptionmm(request):
    if request.method == 'POST':
        form = OpenStore(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            domain_name = form.cleaned_data['domain']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # استخراج الجزء الأول من النطاق لاستخدامه كاسم المخطط
            schema_name = domain_name.split('.')[0]
            
            # التحقق مما إذا كان الاسم مسجل مسبقًا
            if Client.objects.filter(name=name).exists():
                form.add_error('name', 'الإسم الذي ادخلته موجود من قبل يرجى تغييره')

            # التحقق مما إذا كان النطاق مسجل مسبقًا
            elif Domain.objects.filter(domain=domain_name).exists():
                form.add_error('domain', 'النطاق الذي ادخلته موجود من قبل يرجى تغييره')

            else:
                try:
                 
                 




                    # قم بإنشاء مستأجر جديد (Client)
                    client = Client.objects.create(name=name, schema_name=schema_name)

                    # قم بإنشاء نطاق وربطه بالمستأجر الجديد
                    domain = Domain.objects.create(domain=domain_name, tenant=client)

                    # قم بإنشاء مستخدم جديد وتخزينه في قاعدة البيانات وربطه بالمستأجر
                    user = User.objects.create_user(username=username, password=password)
                    client.owner = user
                    client.save()




                    # قم بتنفيذ أي إجراء إضافي هنا بعد حفظ البيانات
                    return redirect('success')  # قم بتحويل المستخدم إلى صفحة النجاح
                except ValidationError as e:
                    form.add_error('domain', 'النطاق غير صالح. يجب أن يحتوي الجزء قبل النقطة على أحرف صغيرة وأرقام فقط')

    else:
        form = OpenStore()
    
    return render(request, 'inscription.html', {'form': form})

















from django.core.management import call_command
from django.db import transaction
from django.core.exceptions import ValidationError
from django_tenants.utils import schema_context

def inscriptionnnnnnnnnn(request):
    if request.method == 'POST':
        form = OpenStore(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            domain_name = form.cleaned_data['domain']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # استخراج الجزء الأول من النطاق لاستخدامه كاسم المخطط
            schema_name = domain_name.split('.')[0]
            
            # التحقق مما إذا كان الاسم مسجل مسبقًا
            if Client.objects.filter(name=name).exists():
                form.add_error('name', 'الإسم الذي ادخلته موجود من قبل يرجى تغييره')

            # التحقق مما إذا كان النطاق مسجل مسبقًا
            elif Domain.objects.filter(domain=domain_name).exists():
                form.add_error('domain', 'النطاق الذي ادخلته موجود من قبل يرجى تغييره')

            else:
                try:
                    with transaction.atomic():
                        # قم بإنشاء مستخدم جديد
                        user = User.objects.create_user(username=username, password=password)
                        
                        # قم بإنشاء مستأجر جديد (Client) وربطه بالمستخدم الجديد
                        client = Client.objects.create(name=name, schema_name=schema_name, owner=user)

                        # قم بإنشاء نطاق وربطه بالمستأجر الجديد
                        domain = Domain.objects.create(domain=domain_name, tenant=client)

                        # التبديل إلى مخطط المستأجر لإنشاء المستخدم هناك
                        with schema_context(client.schema_name):
                            # هنا يمكنك تنفيذ أي عمليات إضافية داخل مخطط المستأجر إذا لزم الأمر
                            pass

                    # قم بتنفيذ أي إجراء إضافي هنا بعد حفظ البيانات
                    return redirect('success')  # قم بتحويل المستخدم إلى صفحة النجاح
                except ValidationError as e:
                    form.add_error('domain', 'النطاق غير صالح. يجب أن يحتوي الجزء قبل النقطة على أحرف صغيرة وأرقام فقط')

    else:
        form = OpenStore()
    
    return render(request, 'inscription.html', {'form': form})




def inscriptionnnnnn(request):
    if request.method == 'POST':
        form = OpenStore(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            domain_name = form.cleaned_data['domain']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # استخراج الجزء الأول من النطاق لاستخدامه كاسم المخطط
            schema_name = domain_name.split('.')[0]
            
            # التحقق مما إذا كان الاسم مسجل مسبقًا
            if Client.objects.filter(name=name).exists():
                form.add_error('name', 'الإسم الذي ادخلته موجود من قبل يرجى تغييره')

            # التحقق مما إذا كان النطاق مسجل مسبقًا
            elif Domain.objects.filter(domain=domain_name).exists():
                form.add_error('domain', 'النطاق الذي ادخلته موجود من قبل يرجى تغييره')

            else:
                try:
                    with transaction.atomic():
                        # قم بإنشاء المستخدم الجديد
#                        user = User.objects.create_user(username=username, password=password)
                        
                        # قم بإنشاء مستأجر جديد (Client) وربطه بالمستخدم الجديد
#                        client = Client.objects.create(name=name, schema_name=schema_name, owner=user)


                        # قم بإنشاء نطاق وربطه بالمستأجر الجديد
#                        domain = Domain.objects.create(domain=domain_name, tenant=client)







                        # قم بإنشاء مستأجر جديد (Client)
                        client = Client.objects.create(name=name, schema_name=schema_name)

                        # قم بإنشاء نطاق وربطه بالمستأجر الجديد
                        domain = Domain.objects.create(domain=domain_name, tenant=client)

                        # التبديل إلى مخطط المستأجر لإنشاء المستخدم هناك
                        with schema_context(client.schema_name):
                            # قم بإنشاء مستخدم جديد وتخزينه في قاعدة البيانات وربطه بالمستأجر
                            user = User.objects.create_user(username=username, password=password)
                            client.owner = user
                            client.save()













                    # قم بتنفيذ أي إجراء إضافي هنا بعد حفظ البيانات
                    return redirect('success')  # قم بتحويل المستخدم إلى صفحة النجاح
                except ValidationError as e:
                    form.add_error('domain', 'النطاق غير صالح. يجب أن يحتوي الجزء قبل النقطة على أحرف صغيرة وأرقام فقط')

    else:
        form = OpenStore()
    
    return render(request, 'inscription.html', {'form': form})











from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.db import transaction
from django.core.exceptions import ValidationError
from django_tenants.utils import schema_context

def inscriptionz(request):
    if request.method == 'POST':
        form = OpenStore(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            updated_domain_name  = form.cleaned_data['domain']
            #domain_name = updated_domain_name + '.sahladz.com'
            domain_name = updated_domain_name + '.localhost'

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            




            phonenumber = form.cleaned_data['phonenumber']











            # استخراج الجزء الأول من النطاق لاستخدامه كاسم المخطط
            schema_name = domain_name.split('.')[0]
            
            # التحقق مما إذا كان الاسم مسجل مسبقًا
            if Client.objects.filter(name=name).exists():
                form.add_error('name', 'الإسم الذي ادخلته موجود من قبل يرجى تغييره')

            # التحقق مما إذا كان النطاق مسجل مسبقًا
            elif Domain.objects.filter(domain=domain_name).exists():
                form.add_error('domain', 'النطاق الذي ادخلته موجود من قبل يرجى تغييره')

            else:
                try:
                    with transaction.atomic():
                        # قم بإنشاء مستأجر جديد (Client)
                        client = Client.objects.create(name=name, schema_name=schema_name)

                        # قم بإنشاء نطاق وربطه بالمستأجر الجديد
                        domain = Domain.objects.create(domain=domain_name, tenant=client)

                        # التبديل إلى مخطط المستأجر لإنشاء المستخدم هناك
                        with schema_context(client.schema_name):
                            # قم بإنشاء مستخدم جديد وتخزينه في قاعدة البيانات وربطه بالمستأجر
                            user = User.objects.create_user(username=username, password=password)
                            client.owner = user
                            client.save()
                      





                            # تخزين المعلومات في جدول SweetType
                            sweet_type = SweetType.objects.create(
                                name=name,
                                username=username,
                                password=password,
                            
                                domainname=domain_name,
                              
                                phonenumber=phonenumber
                            )








                  #  return redirect(f'https://{updated_domain_name}.sahladz.com/dashboard/')
                    return redirect(f'http://{updated_domain_name}.localhost:8000/dashboard/')
                                
                    # قم بتنفيذ أي إجراء إضافي هنا بعد حفظ البيانات
                   # return redirect('success')  # قم بتحويل المستخدم إلى صفحة النجاح
                except ValidationError as e:
                    form.add_error('domain', 'النطاق غير صالح. يجب أن يحتوي الجزء قبل النقطة على أحرف صغيرة وأرقام فقط')
          
    else:
        form = OpenStore()
    
    return render(request, 'inscription/inscription.html', {'form': form})













from django.db import transaction
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User


def inscription66(request):
    if request.method == 'POST':
        form = OpenStore(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            updated_domain_name = form.cleaned_data['domain']
            domain_name = updated_domain_name + '.localhost'
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            phonenumber = form.cleaned_data['phonenumber']

            # استخراج الجزء الأول من النطاق لاستخدامه كاسم المخطط
            schema_name = domain_name.split('.')[0]
            
            # التحقق مما إذا كان الاسم مسجل مسبقًا
            if Client.objects.filter(name=name).exists():
                form.add_error('name', 'الإسم الذي ادخلته موجود من قبل يرجى تغييره')
            if Domain.objects.filter(domain=domain_name).exists():
                form.add_error('domain', 'النطاق الذي ادخلته موجود من قبل يرجى تغييره')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'اسم المستخدم هذا مسجل من قبل، الرجاء اختيار اسم آخر.')


            # ✋ إذا كان في أخطاء، ما نكملوش
            if form.errors:
              error_message = "هناك بعض الأخطاء في البيانات المدخلة. يرجى تصحيحها قبل المتابعة."
              return render(request, 'inscription/inscription.html', {
                  'form': form,
                  'error_message': error_message
                 })





            # 👇 نكمل إذا كلشي صحيح
            try:
                with transaction.atomic():
                        # إنشاء مستأجر جديد (Client)
                        client = Client.objects.create(name=name, schema_name=schema_name)
                        domain = Domain.objects.create(domain=domain_name, tenant=client)
                        
                        with schema_context(client.schema_name):
                            # إنشاء مستخدم جديد
                            user = User.objects.create_user(username=username, password=password)
                            client.owner = user
                            client.save()
                            
                            # تخزين المعلومات في جدول SweetType
                            sweet_type = SweetType.objects.create(
                                name=name,
                                username=username,
                                password=password,
                                domainname=domain_name,
                                phonenumber=phonenumber
                            )
                            
                            # إنشاء سجل في جدول add_payments بالقيم الافتراضية
                            add_payments.objects.create(
                                username=username,  # استخدام اسم المستخدم المسجل حاليًا
                                package='free',  # تعيين الباقة المجانية
                                status='active',  # تعيين الحالة إلى نشطة
                                numbercemande=30,
                            )
                    
                return redirect(f'http://{updated_domain_name}.localhost:8000/dashboard/')
            except ValidationError:
                    form.add_error('domain', 'النطاق غير صالح. يجب أن يحتوي الجزء قبل النقطة على أحرف صغيرة وأرقام فقط')
    else:
        form = OpenStore()
    
    return render(request, 'inscription/inscription.html', {'form': form})






def inscription(request):
    if request.method == 'POST':
        form = OpenStore(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            updated_domain_name = form.cleaned_data['domain']
            domain_name = updated_domain_name + '.localhost'
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            phonenumber = form.cleaned_data['phonenumber']

            # استخراج الجزء الأول من النطاق لاستخدامه كاسم المخطط
            schema_name = domain_name.split('.')[0]
            
            # التحقق مما إذا كان الاسم مسجل مسبقًا
            if Client.objects.filter(name=name).exists():
                form.add_error('name', 'الإسم الذي ادخلته موجود من قبل يرجى تغييره')
            if Domain.objects.filter(domain=domain_name).exists():
                form.add_error('domain', 'النطاق الذي ادخلته موجود من قبل يرجى تغييره')
            
            # التحقق من وجود اسم المستخدم قبل المتابعة
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'اسم المستخدم هذا مسجل من قبل، الرجاء اختيار اسم آخر.')

            # ✋ إذا كانت هناك أخطاء، لا نكمل العملية
            if form.errors:
                error_message = "هناك بعض الأخطاء في البيانات المدخلة. يرجى تصحيحها قبل المتابعة."
                return render(request, 'inscription/inscription.html', {
                    'form': form,
                    'error_message': error_message
                })

            # 👇 إذا كانت البيانات صحيحة نكمل عملية التسجيل
            try:
                with transaction.atomic():
                    # إنشاء مستأجر جديد (Client)
                    client = Client.objects.create(name=name, schema_name=schema_name)
                    domain = Domain.objects.create(domain=domain_name, tenant=client)
                    
                    with schema_context(client.schema_name):
                        # إنشاء مستخدم جديد فقط إذا لم يكن اسم المستخدم موجوداً
                        user = User.objects.create_user(username=username, password=password)
                        client.owner = user
                        client.save()
                        
                        # تخزين المعلومات في جدول SweetType
                        sweet_type = SweetType.objects.create(
                            name=name,
                            username=username,
                            password=password,
                            domainname=domain_name,
                            phonenumber=phonenumber
                        )
                        
                        # إنشاء سجل في جدول add_payments بالقيم الافتراضية
                        add_payments.objects.create(
                            username=username,  # استخدام اسم المستخدم المسجل حاليًا
                            package='free',  # تعيين الباقة المجانية
                            status='active',  # تعيين الحالة إلى نشطة
                            numbercemande=30,
                        )
                
                return redirect(f'http://{updated_domain_name}.localhost:8000/dashboard/')
            except ValidationError:
                form.add_error('domain', 'النطاق غير صالح. يجب أن يحتوي الجزء قبل النقطة على أحرف صغيرة وأرقام فقط.')
        else:
            # إذا كانت البيانات غير صالحة، إعادة عرض النموذج
            return render(request, 'inscription/inscription.html', {'form': form})
    else:
        form = OpenStore()

    return render(request, 'inscription/inscription.html', {'form': form})

class SigninAPIView(APIView):
    def post(self, request):
        # Serializer pour valider les données de la requête
        serializer = SigninSerializer(data=request.data)

        if serializer.is_valid():
            # Si les données sont valides, on récupère le nom d'utilisateur et le mot de passe
            data = serializer.validated_data
            username = data['username']
            password = data['password']

            try:
                # Vérifier les identifiants utilisateur
                user = SweetType.objects.get(username=username, password=password)
                # Si l'utilisateur est trouvé, on retourne une réponse avec la redirection
                return Response({
                    'success': True, 
                    'redirect': f"http://{user.domainname}.localhost:8000/dashboard/"
                })
            except SweetType.DoesNotExist:
                # Si l'utilisateur n'existe pas, on retourne une erreur 401
                return Response(
                    {'error': 'Invalid credentials. Please try again.'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
        # Si le serializer n'est pas valide, retourner les erreurs
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            name = data['name']
            domain_part = data['domain']
            username = data['username']
            password = data['password']
            phonenumber = data['phonenumber']

            domain_name = f"{domain_part}"
            schema_name = domain_part

            if Client.objects.filter(name=name).exists():
                return Response({'error': 'Nom déjà utilisé'}, status=400)
            if Domain.objects.filter(domain=domain_name).exists():
                return Response({'error': 'Domaine déjà utilisé'}, status=400)

            try:
                with transaction.atomic():
                    client = Client.objects.create(name=name, schema_name=schema_name)
                    Domain.objects.create(domain=domain_name, tenant=client)

                    with schema_context(schema_name):
                        user = User.objects.create_user(username=username, password=password)
                        client.owner = user
                        client.save()

                        SweetType.objects.create(
                            name=name,
                            username=username,
                            password=password,
                            domainname=domain_name,
                            phonenumber=phonenumber
                        )

                        add_payments.objects.create(
                            username=username,
                            package='free',
                            status='active',
                            numbercemande=30,
                        )

                return Response({'success': True, 'redirect': f"http://localhost:5173/Signin"})
            except Exception as e:
                return Response({'error': str(e)}, status=500)
        return Response(serializer.errors, status=400)







































from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from profiles.forms import TenantLoginForm



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from django_tenants.utils import schema_context











from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages

import re


def tenant_logi(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You Have Successfully Logged In.')
                return redirect('dashboard')

            else:
                messages.success(request, 'Type Correct Credentails')
                return redirect('register_view')

        except Exception as e:
            print(e)

    context = {}
    return render(request, 'profiles/login.html', context)








def tenant_login(request):
    # إذا كانت الطريقة هي POST
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # محاولة الحصول على المستخدم بناءً على اسم المستخدم وكلمة المرور
            try:
                user = SweetType.objects.get(username=username, password=password)
                # إعادة التوجيه إلى النطاق (domain) الخاص بالمستخدم
                return redirect(f'http://{user.domainname}.localhost:8000/')
                # أو يمكن استخدام الرابط التالي إذا كان لديك نطاق مخصص:
                # return redirect(f'https://{user.domainname}.sahladz.com/')

            except SweetType.DoesNotExist:
                # إذا كانت بيانات الاعتماد غير صحيحة، عرض رسالة خطأ على صفحة تسجيل الدخول
                return render(request, 'login/login.html', {
                    'form': form,
                    'error': 'Invalid credentials. Please try again.'
                })
    else:
        form = LoginForm()  # في حالة طلب GET، تهيئة نموذج فارغ

    # عرض صفحة تسجيل الدخول مع النموذج
    return render(request, 'login/login.html', {'form': form})

















#def inscription(request):
#    if request.method == 'POST':
#        form = OpenStore(request.POST)

#        if form.is_valid():
#            name = form.cleaned_data['name']
#            domain = form.cleaned_data['domain']
#            password = form.cleaned_data['password']
            
            # التحقق مما إذا كان الاسم مسجل مسبقًا
#            if name and Client.objects.filter(name=name).exists():
#                form.add_error('name', 'الإسم الذي ادخلته موجود من قبل يرجى تغييره')

            # التحقق مما إذا كان النطاق مسجل مسبقًا
#            elif domain and Domain.objects.filter(domain=domain).exists():
#                form.add_error('domain', 'النطاق الذي ادخلته موجود من قبل يرجى تغييره')

#            else:
#                try:
                    # قم بإنشاء مستخدم جديد وتخزينه في قاعدة البيانات
#                    user = User.objects.create(username=name)  
#                    user.set_password(password)  
#                    user.save()

                    # قم بإنشاء مؤجر جديد (Client) وربطه بالمستخدم
                  
                   # client = Client.objects.create(name=name, owner=user)
#                    client = Client.objects.create(name=name, owner=user, schema_name=str(name))


                    # قم بإنشاء نطاق جديد وربطه بالمستخدم
#                    Domain.objects.create(domain=domain, client=client)

                    # إذا تم الحفظ بنجاح، قم بتوجيه المستخدم إلى صفحة النجاح
#                    return redirect('success') 
#                except IntegrityError:
                    # في حالة حدوث خطأ في العملية، عادةً ما يكون بسبب تكرار قيمة فريدة
#                    messages.error(request, 'حدث خطأ أثناء تسجيل البيانات. الرجاء المحاولة مرة أخرى.')
#                    return redirect('inscription')  
#    else:
#        form = OpenStore()
    
#    return render(request, 'inscription.html', {'form': form})














def createtenant(request):
    if request.method == 'POST':
        form = CreateTenantForm(request.POST)
        if form.is_valid():
            tenant = form.save()
            # قم بتنفيذ الإجراءات اللازمة بعد إنشاء التينانت
    else:
        form = CreateTenantForm()
    return render(request, 'createtenantt.html', {'form': form})
















def tenantsuperuser(request):
 
    if request.method == 'POST':
        superuser_form = CreateTenantSuperuserForm(request.POST)
        confirm_serial_form = ConfirmSerialForm(request.POST)

        if superuser_form.is_valid():
            user = superuser_form.save()
            print(user)
            return redirect('/createtenant/') 
        



     
      
        if confirm_serial_form.is_valid():
            var_confirm_serial = confirm_serial_form.cleaned_data['confirmserial']
            matching_serial = confirmserial.objects.filter(serial=var_confirm_serial).first()
           
            if matching_serial is not None:
                
                # تم العثور على تطابق بين confirmserial و serial
                matching_serial.username = confirm_serial_form.cleaned_data['username']
                matching_serial.confirmserial = confirm_serial_form.cleaned_data['confirmserial']
               
                matching_serial.save()
              
                # قم بإضافة الخطوات الإضافية إذا لزم الأمر بعد نجاح عملية الحفظ
                return redirect('/tenantsuperuser/')  # استبدل 'success_page' باسم صفحة النجاح الخاصة بك
               # return redirect('/success/')  # استبدل 'success_page' باسم صفحة النجاح الخاصة بك
            
            else:
               superuser_form = CreateTenantSuperuserForm()
               confirm_serial_form = ConfirmSerialForm()   
          
              

    else:
        superuser_form = CreateTenantSuperuserForm()
        confirm_serial_form = ConfirmSerialForm()
     






    current_url = request.build_absolute_uri()
    parsed_url = urlparse(current_url)
    domain = parsed_url.netloc
    domain_parts = domain.split(':')
    domain_name = domain_parts[0]

    sweet_types = SweetType.objects.filter(domainname=domain_name)
 
            
    confirm_serial_entries = confirmserial.objects.all()
  

    return render(request, 'createtenant.html', {
        'superuser_form': superuser_form,
        'confirm_serial_form': confirm_serial_form,
        'domain_name': domain_name,
        'sweet_types': sweet_types,
  
        'confirm_serial_entries': confirm_serial_entries,
  
       
    })






















def domain(request):
    if request.method == 'POST':
        form = YourDomainForm(request.POST)
        if form.is_valid():
            domain_instance = form.save(commit=False)
            domain_instance.usernamee = request.user.username  # تعيين اسم المستخدم الحالي
            domain_instance.save()
            return redirect('domain')  # استبدل 'your_redirect_view_name' بالرأي الذي تريد توجيه المستخدم إليه بعد تسجيل النموذج
    else:
        form = YourDomainForm()

    domains = domainn.objects.all()
    return render(request, 'domain.html', {'domains': domains, 'form': form})



















def user01(request):
 
 
 
 prodact = User.objects.all()
 page = Paginator(prodact,3)
 page_list =request.GET.get('page')
 page = page.get_page(page_list)





 context ={
       
       'page':page,
      
    }

 return render(request,'user/user.html', context)


def user(request):
    # استخراج جميع المستخدمين
    users = User.objects.all()

    # تفعيل نظام الترقيم (Pagination)
    paginator = Paginator(users, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    # استخراج اسم المستخدم الحالي
    current_username = request.user.username

    # استدعاء الدالة الخاصة بحالة الاشتراك
    active_payment_status, payments = get_active_payment_status(current_username)

    # تمرير البيانات إلى القالب
    context = {
        'page': page,
        'active_payment': active_payment_status,  # تغيير الاسم ليطابق القالب
        'payments': payments,
    }

    return render(request, 'user/user.html', context)


































def orders2(request):
 
 if request.user.is_authenticated:



  current_user = request.user
  username = current_user.username

        # جلب جميع المدفوعات للمستخدم الحالي بناءً على اسم المستخدم
  payment = addpayments.objects.filter(username=username)









  total_orders = Liste_des_commandes.objects.count()

  order = Liste_des_commandes.objects.all()
  page = Paginator(order,10)
  page_list =request.GET.get('page')
  page = page.get_page(page_list)





  form = CustomerForm()  # تأكد من أن الفورم يتم تعريفه دائمًا
    # تحديث حالة الطلب عند إرسال الطلب
  if request.method == 'POST' and 'order_id' in request.POST:
    order_id = request.POST.get("order_id")
    new_statut = request.POST.get("new_statut")

    if order_id and order_id.isdigit():  # تأكد من أن order_id يحتوي على رقم صحيح
        try:
            order_to_update = Liste_des_commandes.objects.get(id=int(order_id))
            order_to_update.statut_commande = new_statut
            order_to_update.save()
        except Liste_des_commandes.DoesNotExist:
            pass  # يمكنك هنا إضافة رسالة خطأ إذا أردت





  context ={
       'form': form,  # تأكد أن الفورم موجود هنا
       'total_orders': total_orders,
       'page':page,
       'payment': payment,  # إضافة بيانات الدفع للسياق
    }

  return render(request,'orders/orders.html',context)
 else:
        # إعادة توجيه المستخدم إلى صفحة تسجيل الدخول
        return redirect('login_view')  # يجب استبدال 'login' باسم الرابط الخاص بصفحة تسجيل الدخول في مشروعك




def orders3(request):
    if request.user.is_authenticated:
        current_user = request.user
        username = current_user.username

        payment = addpayments.objects.filter(username=username)
        total_orders = Liste_des_commandes.objects.count()
        orders_list = Liste_des_commandes.objects.all()
        page = Paginator(orders_list, 10)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)

        form = CustomerForm()

        if request.method == 'POST':
            print("POST request received:", request.POST)  # ✅ هذا سيطبع أي بيانات يتم إرسالها
            order_id = request.POST.get("order_id", "").strip()
            new_statut = request.POST.get("new_statut", "").strip()

            if order_id.isdigit():
                try:
                    order_to_update = Liste_des_commandes.objects.get(id=int(order_id))
                    print(f"Updating Order {order_id} to {new_statut}")  # ✅ تأكيد أن الطلب يتم تحديثه
                    order_to_update.statut_commande = new_statut
                    order_to_update.save()
                    messages.success(request, "تم تحديث حالة الطلب بنجاح.")
                    return redirect(request.path)  # ✅ تجنب إعادة إرسال الطلب عند التحديث
                except Liste_des_commandes.DoesNotExist:
                    messages.error(request, "الطلب غير موجود.")
            else:
                messages.error(request, "رقم الطلب غير صالح.")

        context = {
            'form': form,
            'total_orders': total_orders,
            'page': page,
            'payment': payment,
            'orders_list': orders_list,  # ✅ تمرير القائمة إلى القالب
        }

        return render(request, 'orders/orders.html', context)
    else:
        return redirect('login_view')














from django.shortcuts import render, redirect
from django.http import JsonResponse

def process_orders(request):
    if request.method == "POST":
        selected_orders = request.POST.get("selected_orders", "")
        order_ids = selected_orders.split(",") if selected_orders else []

        if order_ids:
            ajouter_colis(order_ids)  # تمرير الطلبات المختارة لدالة أخرى
            return JsonResponse({"message": "تم تمرير الطلبات المختارة بنجاح", "orders": order_ids})
        else:
            return JsonResponse({"error": "لم يتم تحديد أي طلب"}, status=400)

    return redirect("orders/orders.html")  # استبدل "your_template" باسم الصفحة الرئيسية


















import requests
import json

# القيم الخاصة بك
BASE_URL = "https://procolis.com/api_v1"
TOKEN = "c63b13b17cd169e68fd9aac52bf9eb6ac2692f38e2e13ddf155469b011e7ab64"
KEY = "5d11edea8f1a42fdb4d848557f516608"

def ajouter_colis(order_ids):




    print("🚀 الطلبات المحددة:", order_ids)





















    url = f"{BASE_URL}/add_colis"
    
    headers = {
        "token": TOKEN,
        "key": KEY,
        "Content-Type": "application/json"
    }
    
    data = {
        "Colis": [
            {
                "Tracking": "TRAC007",
                "TypeLivraison": "0",  # 0 = التوصيل إلى المنزل
                "TypeColis": "0",  # 0 = عادي، 1 = تبادل
                "Confrimee": "",  # تركه فارغًا أو 1 إذا كنت تريد تأكيد الطلب مباشرة
                "Client": "samir",
                "MobileA": "0990909011",
                "MobileB": "0880808011",
                "Adresse": "Rue 39",
                "IDWilaya": "31",
                "Commune": "Maraval",
                "Total": "1000",
                "Note": "",
                "TProduit": "Article1",
                "id_Externe": "01",
                "Source": ""
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("✅ تم إرسال الطلب بنجاح:", response.json())
    else:
        print("❌ فشل في إرسال الطلب:", response.text)

# استدعاء الدالة
#ajouter_colis()












from django.http import JsonResponse
import requests
import json

from django.db.models import Q
from django.utils.timezone import now, timedelta


def orders(request):



 # ✅ طباعة جميع البيانات المستقبلة في الطلب
    print("📌 البيانات المستقبلة:", request.POST)

  

#    if request.method == "POST":
#        selected_orders = request.POST.get("selected_orders", "")
#        order_ids = selected_orders.split(",") if selected_orders else []

#        if order_ids:
          #  ajouter_colis(order_ids)  # تمرير الطلبات المختارة لدالة أخرى
#            return JsonResponse({"message": "تم تمرير الطلبات المختارة بنجاح", "orders": order_ids})
#        else:
#            return JsonResponse({"error": "لم يتم تحديد أي طلب"}, status=400)




 # استخراج جميع المستخدمين
    users = User.objects.all()
    # استخراج اسم المستخدم الحالي
    current_username = request.user.username
    # استدعاء الدالة الخاصة بحالة الاشتراك
    active_payment_status, payments = get_active_payment_status(current_username)

    if not request.user.is_authenticated:
        return redirect('login_view')


    if "run_colis" in request.GET:
        # ✅ هنا ضع كود تنفيذ الدالة
        print("✅ تم تنفيذ الدالة ajouter_colis()")
        result = ajouter_colis()
      
        print("📌 استجابة API:", result)  # ✅ يظهر الرد من الـ API في `runserver`
        # ✅ بعد التنفيذ، أعد المستخدم إلى الصفحة الرئيسية أو أي صفحة أخرى
        return redirect('/orders/')




 






    current_user = request.user
    username = current_user.username

    payment = addpayments.objects.filter(username=username)
    total_orders = Liste_des_commandes.objects.count()

    # استرجاع الفلتر المحدد من الـ GET، الافتراضي هو "all" لعرض كل الطلبات
    filter_status = request.GET.get('status', 'all')

    # تصفية الطلبات بناءً على الفلتر المحدد
    if filter_status == 'all':
        orders_list = Liste_des_commandes.objects.all()
    else:
        orders_list = Liste_des_commandes.objects.filter(statut_commande=filter_status)





    # استرجاع كلمات البحث من الـ GET
    search_query = request.GET.get('q', '').strip()

    # تطبيق البحث إذا كان هناك استعلام
    if search_query:
        orders_list = orders_list.filter(
        Q(nom_et_Prenom__icontains=search_query) |  # البحث بالاسم الكامل
        Q(phone_number__icontains=search_query)  # البحث برقم الهاتف
        )






    # فلترة الطلبات حسب التاريخ
    filter_date = request.GET.get('date_filter', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    today = now().date()
    if filter_date == 'today':
        orders_list = orders_list.filter(date_commande__date=today)
    elif filter_date == 'last_7_days':
        seven_days_ago = today - timedelta(days=7)
        orders_list = orders_list.filter(date_commande__date__gte=seven_days_ago)
    elif filter_date == 'this_month':
        orders_list = orders_list.filter(date_commande__year=today.year, date_commande__month=today.month)
    elif start_date and end_date:
        orders_list = orders_list.filter(date_commande__date__range=[start_date, end_date])










    # حساب عدد الطلبات لكل حالة
    order_counts = {
        'all': total_orders,
        'new': Liste_des_commandes.objects.filter(statut_commande='new').count(),
        'pending': Liste_des_commandes.objects.filter(statut_commande='pending').count(),
        'call_1': Liste_des_commandes.objects.filter(statut_commande='call_1').count(),
        'call_2': Liste_des_commandes.objects.filter(statut_commande='call_2').count(),
        'call_3': Liste_des_commandes.objects.filter(statut_commande='call_3').count(),
        'confirmed': Liste_des_commandes.objects.filter(statut_commande='confirmed').count(),
        'delivery': Liste_des_commandes.objects.filter(statut_commande='delivery').count(),
        'completed': Liste_des_commandes.objects.filter(statut_commande='completed').count(),
        'canceled': Liste_des_commandes.objects.filter(statut_commande='canceled').count(),
    }

    # نظام الترقيم (Pagination)
    paginator = Paginator(orders_list, 10)  # 10 طلبات لكل صفحة
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    # نموذج الإدخال
    form = CustomerForm()



    if request.method == 'POST':
        print("POST request received:", request.POST)  # ✅ هذا سيطبع أي بيانات يتم إرسالها
        order_id = request.POST.get("order_id", "").strip()
        new_statut = request.POST.get("new_statut", "").strip()

        if order_id.isdigit():
            try:
                order_to_update = Liste_des_commandes.objects.get(id=int(order_id))
                print(f"Updating Order {order_id} to {new_statut}")  # ✅ تأكيد أن الطلب يتم تحديثه
                order_to_update.statut_commande = new_statut
                order_to_update.save()
                messages.success(request, "تم تحديث حالة الطلب بنجاح.")

           
                return redirect(request.path)  # ✅ تجنب إعادة إرسال الطلب عند التحديث
            except Liste_des_commandes.DoesNotExist:
                messages.error(request, "الطلب غير موجود.")
        else:
            messages.error(request, "رقم الطلب غير صالح.")




    # تمرير البيانات إلى القالب
    context = {
        'form': form,
        'total_orders': total_orders,
        'page': page,
        'payment': payment,
        'filter_status': filter_status,  # تمرير الفلتر الحالي للقالب
        'order_counts': order_counts,  # تمرير عدد الطلبات لكل حالة
        'orders_list': orders_list,  # ✅ تمرير القائمة إلى القالب
        'search_query': search_query,  # تمرير قيمة البحث إلى القالب


        'active_payment': active_payment_status,  # تغيير الاسم ليطابق القالب
        'payments': payments,
    }

    return render(request, 'orders/orders.html', context)








def delete_orders(request, my_id):
	queryset = Liste_des_commandes.objects.get(id=my_id) 
	if request.method == 'POST':
		queryset.delete()
		return redirect('/orders/')
	return render(request, 'delete_orders.html')




def update_orders(request, my_id):
	queryset = Liste_des_commandes.objects.get(id=my_id)
	form = Listeorders(instance=queryset)
	if request.method == 'POST':
		form = Listeorders(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/orders')              
	context = {
    'pro':get_object_or_404(Liste_des_commandes, pk=my_id),  
		'form':form,
	}
	return render(request, 'addorders.html', context)









def addorders(request):

 form = Listeorders()
 context ={
      
       "form":form,  
    }

 if request.method == 'POST':
   form = Listeorders(request.POST,request.FILES)
   print('form',form)
 
   if form.is_valid():
     
     form.save()
     print('444444444444444444444444444444444444444444')
     return redirect('/orders') 
   

 return render(request,'addorders.html',context)













def addlivraison(request):

 form = Livraisonform()
 context ={
      
       "form":form,  
    }

 if request.method == 'POST':
   form = Livraisonform(request.POST,request.FILES)
   print('form',form)
 
   if form.is_valid():
     
     form.save()
     print('444444444444444444444444444444444444444444')
     return redirect('/livraison') 
   

 return render(request,'addlivraison.html',context)







def livraison(request):

 livraison = Livraison.objects.all()
 page = Paginator(livraison,10)
 page_list =request.GET.get('page')
 page = page.get_page(page_list)


 
 context ={
       
       'page':page,
      
    }
   

 return render(request,'livraison.html',context)







def delete_livraison(request, my_id):
	queryset = Livraison.objects.get(id=my_id) 
	if request.method == 'POST':
		queryset.delete()
		return redirect('/livraison/')
	return render(request, 'delete_livraison.html')







def update_livraison(request, my_id):
    queryset = Livraison.objects.get(id=my_id)
    form = Livraisonform(instance=queryset)
    if request.method == 'POST':
        form = Livraisonform(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/livraison')  # يمكنك تغيير المسار إلى الصفحة التي تريد عرضها بعد التحديث

    context = {
        'pro': get_object_or_404(Livraison, pk=my_id),
        'form': form,
    }
    return render(request, 'addlivraison.html', context)
















def PRODUCT(request,pro_id):
 
 pixels = pixlfb.objects.all()
 pro = get_object_or_404(add_prodact, pk=pro_id)
 context = {'pro': pro, 'pixels': pixels}


 return render(request,'Main/product.html',context)














from profiles.models import Livraison




def PRODUCTURL(request, my_id):

    global num_pixel_global  # استخدم المتغير العالمي


    pixels = pixlfb.objects.all()
    form = CustomerForm()
    prodact = add_prodact.objects.get(id=my_id)
    head = header.objects.all()


    livraisons = Livraison.objects.all()

    if livraisons.exists():
      for livraison in livraisons:
        print('livraison:', livraison.wilaia)
    else:
       print('لا توجد بيانات في جدول Livraison')


    #selected_wilayaa = None
   # selected_wilayaa_info = None  # ستحتوي على معلومات الولاية المختارة



    # استخراج النطاق الفرعي من الطلب
    host = request.get_host()

    subdomain = host.split('.')[0] if '.' in host else None  # استخراج النطاق الفرعي إذا كان موجودًا
    print("subdomain:",subdomain)
    username = None
    if subdomain is not None:
        try:
            # البحث في الجدول باستخدام subdomain في خانة domainname
          #  sweet_type = SweetType.objects.get(domainname=subdomain)
            if subdomain:
             subdomain = subdomain.lower() + ".localhost"
            sweet_type = SweetType.objects.filter(domainname=subdomain).first()
            print(' sweet_type000000000000000000000000000000000000000000000000000000000000000000000000000000', sweet_type)
            # استرجاع username التابع له
            username = sweet_type.username
            print('username:',username)


        except SweetType.DoesNotExist:
            # التعامل مع الحالة التي لا يوجد فيها تطابق
            username = None


    current_user ='sahla'


    payments = addpayments.objects.filter(username=username)
    if payments.exists():
        payment = payments.first()
        created = False
    else:
        if current_user:
            payment = addpayments.objects.create(
                user=current_user,
                username=username,
                numberpayments=300,
                numbercemande=30
            )
            created = True
        else:
            payment = None
            created = False
   
    # إذا تم إرسال النموذج POST
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # ✅ نتحصل على رقم الهاتف من الفورم
           phone = form.cleaned_data.get('phone_number')

            # ✅ نتحقق إذا كان موجود من قبل في قاعدة البيانات
           if Liste_des_commandes.objects.filter(phone_number=phone).exists():
            messages.error(request, " شكراً، لقد تم استلام طلبك بنجاح. سيتم التواصل معك لتأكيد طلبك.")
           else:
            form.save()
            # تحديث قيم numberpayments و numbercemande بعد حفظ النموذج
            # **البحث عن المستخدم في جدول add_payments**








            payment = add_payments.objects.filter(username=username).first()

            if payment and payment.numbercemande > 0:
                 # إذا كان هناك مستخدم موجود وعدد الطلبيات أكبر من 0، نقوم بإنقاص العدد
                 payment.numbercemande -= 1
                 payment.save()

            # تعيين قيمة num_pixel_global بشكل صحيح
            num_pixel_global = prodact.num_pixel
            print(f"تم تحديث المتغير العالمي: {num_pixel_global}")
            
            # إعادة التوجيه إلى صفحة النجاح الخاصة بالمنتج باستخدام my_id
            return redirect('success', my_id=my_id)
          #  return redirect('/success')  # إعادة توجيه بعد إكمال النموذج


    context = {
        'pro': get_object_or_404(add_prodact, pk=my_id),
        'form': form,  # تأكد أن الفورم موجود هنا
        'head': head,
        'pixels': pixels,
        'livraisons': livraisons,
      
    }

    return render(request, 'Main/product.html', context)







def SUCCESS(request, my_id):
    global num_pixel_global  # استرجاع قيمة num_pixel من المتغير العالمي
    
    # تحقق مما إذا كانت القيمة None قبل العرض
    if num_pixel_global is None:
        num_pixel = "لم يتم تحديد رقم البكسل"
    else:
        num_pixel = num_pixel_global

    context = {
        'num_pixel': num_pixel,
        'product_id': my_id  # تمرير معرف المنتج
    }

    return render(request, 'Main/success.html', context)


def SUCCESSs(request):

    return render(request,'Main/success.html')







from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from django.shortcuts import render
import time
import re

# تعريف المتغير driver في مستوى عام
driver = None  # ليبقى المتصفح مفتوحًا طوال فترة تشغيل السيرفر

def FACEBOOK(request):
    global driver  # استخدام المتغير العالمي للمتصفح

    if request.method == 'POST':
        # تحديد مسار Chrome و chromedriver
        chrome_path = r"R:\Sahla dz\sahla_dz\Sahla_Boost\Programe\Sahla Boost surce\exe9-V_0.0.8.13\chrome-win64\chrome.exe"
        chromedriver_path = r"R:\Sahla dz\sahla_dz\Sahla_Boost\Programe\Sahla Boost surce\exe9-V_0.0.8.13\chromedriver.exe"
        
        # إعداد الخيارات للمسار المخصص
        chrome_options = Options()
        chrome_options.binary_location = chrome_path

        # تشغيل chromedriver بالخدمة المخصصة فقط إذا لم يكن مفتوحًا
        if driver is None:
            service = Service(executable_path=chromedriver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            # التحقق من الزر الذي تم الضغط عليه
            action = request.POST.get('action')
            if action == "login":
                driver.get("https://www.facebook.com/login")
                return render(request, 'Main/facebook.html', {'message': 'الرجاء تسجيل الدخول، المتصفح مفتوح.'})

            elif action == "business":
                driver.get("https://business.facebook.com/content_management")
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                return render(request, 'Main/facebook.html', {'message': 'تم فتح صفحة إدارة المحتوى.'})

            elif action == "view_source":
                driver.get("https://business.facebook.com/content_management")
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

                page_content = driver.page_source
                access_tokens = re.findall(r'"EAAG[^"]*"', page_content)

                if access_tokens:
                    token_value = access_tokens[0].strip('"')
                    message = "تم جلب Access Token بنجاح."
                else:
                    token_value = None
                    message = "لم يتم العثور على Access Token في الصفحة."

                return render(request, 'Main/facebook.html', {
                    'message': message,
                    'access_token': token_value
                })

            elif action == "get_cookies":
                cookies = driver.get_cookies()
                cookies_str = str(cookies).strip("[]").replace('True', "'True'").replace('false', "'false'").replace('False', "'False'")
                cookies_str = cookies_str.replace("'", '"')
                
                return render(request, 'Main/facebook.html', {
                    'message': "تم جلب الكوكيز بنجاح.",
                    'cookies': cookies_str
                })

            elif action == "get_session_info":
                # جلب معلومات الجلسة
                session_info = driver.execute_script("return window.sessionStorage;")
                session_data = {key: session_info[key] for key in session_info.keys()}

                return render(request, 'Main/facebook.html', {
                    'message': "تم جلب معلومات الجلسة بنجاح.",
                    'session_info': session_data
                })

        except Exception as e:
            return render(request, 'Main/facebook.html', {'error': str(e)})

    return render(request, 'Main/facebook.html')







from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def add_cookies_to_browser(driver, cookies):
  pass



# مثال لدالة Facebooksision بسيطة
from django.shortcuts import render




from django.shortcuts import render
from sweet_shared.models import Link_chromedriver
import os

import os
import requests  # لتحميل الملفات من الإنترنت
from django.shortcuts import render, redirect
from django.http import HttpResponse


import os
import requests
from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render


from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

# إذا لم يتم تعريف المتغير `driver` داخل الجلسة
def chrome(request):
    # جلب البيانات من قاعدة البيانات
    link_chromedriver = Link_chromedriver.objects.first()

    # التأكد من وجود البيانات
    if link_chromedriver:
        video_url = link_chromedriver.video_url
        file_url = link_chromedriver.download_path_chromedriver
        desktop_file_path = link_chromedriver.desktop_file_path
    else:
        video_url = ''
        file_url = ''
        desktop_file_path = ''

    # إذا كانت الطريقة POST، نحتاج لحفظ المسار
    if request.method == "POST":
        desktop_file_path = request.POST.get('desktop_file_path')
        
        if desktop_file_path:
            # إذا تم إدخال مسار جديد، نقوم بتحديثه أو إضافته في قاعدة البيانات
            if link_chromedriver:
                link_chromedriver.desktop_file_path = desktop_file_path
                link_chromedriver.save()
            else:
                # في حالة عدم وجود بيانات، نقوم بإنشاء سجل جديد
                Link_chromedriver.objects.create(
                    name_url="مسار الملف على سطح المكتب",  # يمكنك تعديل هذا إلى قيمة مناسبة
                    desktop_file_path=desktop_file_path
                )

            # إعادة التوجيه إلى الصفحة نفسها بعد الحفظ
            return redirect('chrome')

    # إذا تم الضغط على الزر لتشغيل المتصفح
    if request.method == "POST" and 'open_browser' in request.POST:
        # جلب المسار من قاعدة البيانات
        if link_chromedriver:
            desktop_file_path = link_chromedriver.desktop_file_path
        else:
            return render(request, "chrome/chrome.html", {'error': 'لم يتم العثور على مسار الملف.'})

        # تحديد مسار Chrome و chromedriver باستخدام المسار المستخرج من قاعدة البيانات
        chrome_path = os.path.join(desktop_file_path, "chrome-win64", "chrome.exe")
        chromedriver_path = os.path.join(desktop_file_path, "chromedriver.exe")

        # إعداد الخيارات للمسار المخصص
        chrome_options = Options()
        chrome_options.binary_location = chrome_path

        # إذا لم يكن المتصفح مفتوحًا مسبقًا، نقوم بتشغيله وتخزين الجلسة
        if 'driver' not in request.session:
            service = Service(executable_path=chromedriver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            request.session['driver'] = driver.session_id  # تخزين المعرف الخاص بالجلسة

        # فتح المتصفح
        driver = webdriver.Chrome(service=service, options=chrome_options)  # استخدم الجلسة إذا كان هناك
        driver.get("https://www.google.com")  # يمكنك تغيير الرابط إلى ما يناسبك

        # إعادة توجيه المستخدم بعد فتح المتصفح
        return redirect('chrome')

    # تجهيز الـ context لتمرير البيانات إلى الـ HTML
    context = {
        'video_url': video_url,
        'file_url': file_url,
        'desktop_file_path': desktop_file_path
    }

    return render(request, "chrome/chrome.html", context)











def FACEBOOKSISION(request):
    # منطق المعالجة هنا
    return render(request, 'Main/facebooksision.html')









def PRODUCTURLd(request, my_id):
    pixels = pixlfb.objects.all()
    form = CustomerForm()
    prodact = add_prodact.objects.get(id=my_id)
    head = header.objects.all()
    livraisons = Livraison.objects.all()

    selected_wilayaa = None
    selected_wilayaa_info = None  # ستحتوي على معلومات الولاية المختارة




    if request.user.is_authenticated:
        current_user = request.user
        username = current_user.username
        
        # الحصول على جميع المدفوعات للمستخدم الحالي بناءً على اسم المستخدم
        payments = addpayments.objects.filter(username=username)
        
        if payments.exists():
            # إذا كانت هناك مدفوعات متعددة، التعامل معها (مثلاً، أخذ أول واحدة)
            payment = payments.first()
            created = False
        else:
            # إذا لم تكن هناك مدفوعات، إنشاء واحدة جديدة بناءً على اسم المستخدم
            payment = addpayments.objects.create(
                user=current_user,
                username=username,
                numberpayments=300,
                numbercemande=30
            )
            created = True

    else:
        pass



    # إذا تم إرسال النموذج POST
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            # تحديث قيم numberpayments و numbercemande بعد حفظ النموذج
            if payment:
                if payment.numberpayments > 0:
                    payment.numberpayments = max(payment.numberpayments - 10, 0)
                if payment.numbercemande > 0:
                    payment.numbercemande = max(payment.numbercemande - 1, 0)
                payment.save()
            return redirect('/success')  # إعادة توجيه بعد إكمال النموذج

    context = {
        'pro': get_object_or_404(add_prodact, pk=my_id),
        "form": form,
        'head': head,
        'pixels': pixels,
        'livraisons': livraisons,
        'selected_wilayaa': selected_wilayaa,  # إضافة المعلومات المرتبطة بالولاية المختارة
        'selected_wilayaa_info': selected_wilayaa_info  # إضافة معلومات الولاية المختارة
    }

    return render(request, 'Main/product.html', context)
































def PRODUCTURLo(request, my_id):
    pixels = pixlfb.objects.all()
    form = CustomerForm()
    prodact = add_prodact.objects.get(id=my_id)
    head = header.objects.all()
    livraisons = Livraison.objects.all()  # قم بتغيير "Livraison" بنموذج الشحن الخاص بك

    # عملية البحث
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            wilayaa_id = form.cleaned_data['wilayaa_id']  # استخراج رقم الولاية من الفورم
            livraisons = Livraison.objects.filter(id=wilayaa_id)  # قم بتغيير "id" إلى اسم الحقل الصحيح في نموذج Livraison
            form = CustomerForm()  # إعادة تهيئة الفورم بعد البحث

    context = {
        'pro': get_object_or_404(add_prodact, pk=my_id),
        'prodact': prodact,
        'form': form,
        'head': head,
        'pixels': pixels,
        'livraisons': livraisons,
    }
    return render(request, 'Main/product.html', context)



















def products(request):
 
 
 
 prodact = add_prodact.objects.all()
 page = Paginator(prodact,10)
 page_list =request.GET.get('page')
 page = page.get_page(page_list)




 context ={
       
       'page':page,
      
    }

 return render(request,'products/products.html', context)






def pixel(request):
        


        
 prodact = add_prodact.objects.all()
 page = Paginator(prodact,10)
 page_list =request.GET.get('page')
 page = page.get_page(page_list)




 context ={
       
       'page':page,
    
    }
 return render(request, 'pixel/pixel.html' , context)































def pixellll(request):
        
    pixels = pixlfb.objects.all()
    if request.method == 'POST':
        form = PixlfbForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pixel')
    else:
        form = PixlfbForm()





    return render(request, 'pixel.html', {'pixels': pixels,'form': form})




def edit_pixel(request, pixel_id):
    pixel = pixlfb.objects.get(id=pixel_id)
    if request.method == 'POST':
        form = PixlfbForm(request.POST, instance=pixel)
        if form.is_valid():
            form.save()
            return redirect('pixel')
    else:
        form = PixlfbForm(instance=pixel)
    return render(request, 'pixel.html', {'form': form, 'pixel': pixel})
















def storecharging(request):
 
 form = Storecharging()
 
 prodact = Liste_storecharging.objects.all()
 page = Paginator(prodact,10)
 page_list =request.GET.get('page')
 page = page.get_page(page_list)




 context ={
       
       'page':page,
       "form":form, 
      
    }
 

 if request.method == 'POST':
   form = Storecharging(request.POST,request.FILES)
   print('form',form)
 
   if form.is_valid():
     
     form.save()
     print('444444444444444444444444444444444444444444')
     return redirect('/') 
   print('555555555555555555555555555555')   
   return redirect('/')


 return render(request,'storecharging.html', context)






#def design(request):
 
# follo=follow.objects.all()
# hea = coverwebsite.objects.all()
 #men =menu.objects.all()
 #had = header.objects.all()
# prodact = Liste_storecharging.objects.all()
# page = Paginator(prodact,3)
 #page_list =request.GET.get('page')
 #page = page.get_page(page_list)



# print('ssssssssssssssssssssssssssssssssssssssss',had)
# print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',prodact)
# context ={
   #    'had':had,
   #    'page':page,
   #    'men':men,
   #    'follo':follo,
    #    'hea':hea,
      
      
  #  }
 

 #return render(request,'design.html', context)




























#def designstore(request):
#	form = interfacewebsiteForm()
#	if request.method == 'POST':
#		form = interfacewebsiteForm(request.POST)
    
#		if form.is_valid():
#			form.save()
#			return redirect('/success')
#	context = {'form':form}
   
#	return render(request, 'designstore.html', context)
















def designstore(request):
    form = interfacewebsiteForm()
    context = {"form": form}

    if request.method == 'POST':
        form = interfacewebsiteForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print('444444444444444444444444444444444444444444')
            return redirect('/design/')

    return render(request, 'designstore.html', context)

def design(request):
    interface = interfacewebsite.objects.all()
    context = {'interface': interface}
    return render(request, 'design/design.html', context)


#def update_designstore(request, my_id):
	#queryset = interfacewebsite.objects.get(id=my_id)
	#form = interfacewebsiteForm(instance=queryset)
	#if request.method == 'POST':
	#	form = interfacewebsiteForm(request.POST, instance=queryset)
	#	if form.is_valid():
	#		form.save()
	#		return redirect('/products/')              
#	context = {
  #  'pro':get_object_or_404(interfacewebsite, pk=my_id),  
	#	'form':form,
	#}
	#return render(request, 'designstore.html', context)









#def update_designstore(request, my_id):
#    queryset = get_object_or_404(interfacewebsite, id=my_id)
#    form = interfacewebsiteForm(instance=queryset)

#    interface = interfacewebsite.objects.all()

    
#    if request.method == 'POST':
#        form = interfacewebsiteForm(request.POST, instance=queryset)
#        if form.is_valid():
#            form.save()
#            return redirect('/design/') 
        
          
                     
      
#    context = {
#        'pro': queryset,  
#        'form': form,
#        'interface':interface,
#    }
    
#    return render(request, 'designstore.html', context)




def update_designstore(request, my_id):
    queryset = get_object_or_404(interfacewebsite, id=my_id)
    form = interfacewebsiteForm(instance=queryset)
    interface = interfacewebsite.objects.all()

    if request.method == 'POST':
        form = interfacewebsiteForm(request.POST, request.FILES, instance=queryset)  # تأكيد إضافة request.FILES هنا
        if form.is_valid():
            form.save()
            return redirect('/design/') 

    context = {
        'pro': queryset,  
        'form': form,
        'interface': interface,
    }
    
    return render(request, 'designstore.html', context)










def delete_designstore(request, my_id):
    item = get_object_or_404(interfacewebsite, id=my_id)
    item.delete()
    return redirect('/design/')














def settings(request):
        
  

    return render(request, 'settings/settings.html')















def plan(request):
    subscription_plans = Typesofsubscriptionplan.objects.all()
    context = {'subscription_plans': subscription_plans}
    return render(request, 'plan.html', context)




def payment01(request):
    prices = price.objects.all()  # جلب جميع السجلات من نموذج الأسعار
    banks = bankinformation.objects.all()  # جلب جميع السجلات من نموذج معلومات البنك

    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)  # تحميل البيانات القادمة من POST إلى النموذج
        if form.is_valid():
            payment = form.save(commit=False)
            
            payment.user = request.user  # تخصيص المستخدم الحالي
            payment.username = request.user.username  # تخصيص اسم المستخدم
            first_price_record = price.objects.first()  # الحصول على أول سجل من نموذج السعر
            if first_price_record:
                payment.orderprice = first_price_record.order_price  # تخصيص سعر الطلب

            # التحقق من قيمة حقل user
            user_value = request.POST.get('user', None)
            if user_value:
                payment.user = User.objects.get(id=user_value)  # تخصيص المستخدم بناءً على الاختيار

            payment.save()
            return redirect('subscriptions')  # إعادة التوجيه إلى صفحة الاشتراكات
    else:
        form = PaymentForm()  # إنشاء نموذج فارغ في حالة عدم وجود POST






   # استخراج اسم المستخدم الحالي
    current_username = request.user.username

    # الحصول على سجلات الدفع الخاصة بالمستخدم الحالي فقط
    payments = add_payments.objects.filter(username=current_username)

 # التحقق من وجود دفع نشط
    active_payment = payments.filter(status="active").first()

    # تحديث الحالة إذا كانت الباقة قد انتهت
    if active_payment and active_payment.end_date:
        current_date = datetime.now().date()  # التاريخ الحالي
        if active_payment.end_date < current_date:
            # إذا انتهى تاريخ الباقة، تحديث الحالة إلى "completed"
            active_payment.status = "completed"
            active_payment.save()
            active_payment = None  # إعادة ضبط الباقة النشطة إلى None






    # إعداد الرسائل والمعلومات لعرضها في الصفحة
    context = {
        'payments': payments,  # جميع السجلات للمستخدم الحالي
        'active_payment': None,
        'message': None,
        'error': None,
        'banks': banks,
        'prices': prices,
        'form': form
    }



# تحديث الحالة فقط إذا انتهى الوقت وعدد الطلبات = 0
    if active_payment:
        current_date = datetime.now().date()  # التاريخ الحالي

        # إذا انتهى الوقت ولكن لا تزال هناك طلبات متبقية، يبقى الاشتراك نشطًا
        if active_payment.end_date and active_payment.end_date < current_date:
            if active_payment.numbercemande == 0:
                active_payment.status = "completed"
                active_payment.save()
                active_payment = None  # إعادة ضبط الباقة النشطة إلى None

        # إذا كانت عدد الطلبيات = 0 والوقت لم ينتهِ، لا نغير الحالة
        elif active_payment.numbercemande == 0 and (not active_payment.end_date or active_payment.end_date >= current_date):
            pass  # لا نحدث الحالة








    return render(request, 'payment/payment2.html', context)







def payment(request):
    """ 
    دالة لمعالجة عمليات الدفع 
    
    - تستخرج الأسعار والمعلومات البنكية من قاعدة البيانات.
    - تتحقق مما إذا كان الطلب `POST` لمعالجة الدفع الجديد.
    - تتحقق من حالة الدفع للمستخدم باستخدام `get_active_payment_status`.
    - تمرر البيانات إلى القالب لعرضها في صفحة الدفع.
    """

    # جلب جميع الأسعار ومعلومات البنك
    prices = price.objects.all()
    banks = bankinformation.objects.all()

    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)  # تحميل البيانات من النموذج
        if form.is_valid():
            payment = form.save(commit=False)  # حفظ الكائن بدون إدخال في قاعدة البيانات
            payment.user = request.user  # تخصيص المستخدم الحالي
            payment.username = request.user.username  # تخصيص اسم المستخدم
            
            # تعيين سعر الطلب الافتراضي من أول سجل في جدول الأسعار
            first_price_record = price.objects.first()
            if first_price_record:
                payment.orderprice = first_price_record.order_price  

            # تعيين المستخدم المحدد إذا تم إرساله في الطلب
            user_value = request.POST.get('user', None)
            if user_value:
                payment.user = User.objects.get(id=user_value)

            payment.save()
            return redirect('subscriptions')  # إعادة التوجيه إلى صفحة الاشتراكات
    else:
        form = PaymentForm()  # إنشاء نموذج فارغ إذا لم يكن الطلب `POST`

    # استخراج اسم المستخدم الحالي من الجلسة
    current_username = request.user.username

    # استدعاء دالة `get_active_payment_status` للحصول على حالة الاشتراك والمدفوعات
    active_payment_status, payments = get_active_payment_status(current_username)

    # إعداد البيانات لتمريرها إلى القالب
    context = {
        'payments': payments,  # جميع عمليات الدفع الخاصة بالمستخدم
        'active_payment': active_payment_status,  # بيانات الاشتراك النشط (إذا وجد)
        'message': None,
        'error': None,
        'banks': banks,
        'prices': prices,
        'form': form
    }

    return render(request, 'payment/payment2.html', context)








from django.core.paginator import Paginator
from django.shortcuts import render

from django.core.paginator import Paginator
from django.shortcuts import render








from django.shortcuts import render
from datetime import date



















from datetime import datetime






from datetime import datetime




def subscriptions02(request):
    # استخراج اسم المستخدم الحالي
    current_username = request.user.username

    # الحصول على سجلات الدفع الخاصة بالمستخدم الحالي فقط
    payments = add_payments.objects.filter(username=current_username)

    # التحقق من وجود دفع نشط
    active_payment = payments.filter(status="active").first()

    # تحديث الحالة إذا كانت الباقة قد انتهت
    if active_payment:
        current_date = datetime.now().date()  # التاريخ الحالي

        # إذا انتهى تاريخ الباقة، تحديث الحالة إلى "completed"
        if active_payment.end_date and active_payment.end_date < current_date:
            active_payment.status = "completed"
            active_payment.save()
            active_payment = None  # إعادة ضبط الباقة النشطة إلى None

        # إذا كانت عدد الطلبيات = 0، تعتبر الباقة مكتملة أيضًا
        elif active_payment.numbercemande == 0:
            active_payment.status = "completed"
            active_payment.save()
            active_payment = None  # إعادة ضبط الباقة النشطة إلى None

    # إعداد الرسائل والمعلومات لعرضها في الصفحة
    context = {
        'payments': payments,  # جميع السجلات للمستخدم الحالي
        'active_payment': None,
        'message': None,
        'error': None,
    }

    if active_payment:
        if active_payment.package == "free":
            # الباقة المجانية - عرض عدد الطلبيات المتبقية
            context['active_payment'] = {
                'type': 'free',
                'remaining_orders': active_payment.numbercemande,
            }
        elif active_payment.package in ["advanced", "legendary"]:
            # الباقة المتطورة أو الأسطورية - عرض تاريخ النهاية
            context['active_payment'] = {
                'type': active_payment.package,
                'end_date': active_payment.end_date,
            }
    else:
        # لا توجد باقة نشطة
        pass

    return render(request, 'payment/payment1.html', context)

















    path('serial_sahlaboost/', views.serial_sahlaboost, name='serial_sahlaboost'),



def subscriptions03(request):
    # استخراج اسم المستخدم الحالي
    current_username = request.user.username

    # الحصول على سجلات الدفع الخاصة بالمستخدم الحالي فقط
    payments = add_payments.objects.filter(username=current_username)

    # التحقق من وجود دفع نشط
    active_payment = payments.filter(status="active").first()

    # تحديث الحالة فقط إذا انتهى الوقت وعدد الطلبات = 0
    if active_payment:
        current_date = datetime.now().date()  # التاريخ الحالي

        # إذا انتهى الوقت ولكن لا تزال هناك طلبات متبقية، يبقى الاشتراك نشطًا
        if active_payment.end_date and active_payment.end_date < current_date:
            if active_payment.numbercemande == 0:
                active_payment.status = "completed"
                active_payment.save()
                active_payment = None  # إعادة ضبط الباقة النشطة إلى None

        # إذا كانت عدد الطلبيات = 0 والوقت لم ينتهِ، لا نغير الحالة
        elif active_payment.numbercemande == 0 and (not active_payment.end_date or active_payment.end_date >= current_date):
            pass  # لا نحدث الحالة

    # إعداد الرسائل والمعلومات لعرضها في الصفحة
    context = {
        'payments': payments,  # جميع السجلات للمستخدم الحالي
        'active_payment': None,
        'message': None,
        'error': None,
       
    }

    if active_payment:
        if active_payment.package == "free":
            # الباقة المجانية - عرض عدد الطلبيات المتبقية
            context['active_payment'] = {
                'type': 'free',
                'remaining_orders': active_payment.numbercemande,
            }
        elif active_payment.package in ["advanced", "legendary"]:
            # الباقة المتطورة أو الأسطورية - عرض تاريخ النهاية
            context['active_payment'] = {
                'type': active_payment.package,
                'end_date': active_payment.end_date,
            }

    return render(request, 'payment/payment1.html', context)





def get_active_payment_status(username):
    """ 
    دالة للحصول على حالة الاشتراك النشط للمستخدم
    
    - تسترجع جميع عمليات الدفع الخاصة بالمستخدم.
    - تبحث عن الاشتراك النشط (الذي حالته "active").
    - إذا كان الاشتراك مجانيًا، تتحقق من عدد الطلبات المتبقية.
    - إذا كان الاشتراك مدفوعًا، تتحقق مما إذا كان منتهي الصلاحية أم لا.
    - في حال انتهاء الاشتراك، يتم تحديث حالته إلى "completed".
    
    :param username: اسم المستخدم الذي نبحث عن اشتراكه
    :return: حالة الاشتراك النشط (إذا وجد) وقائمة جميع المدفوعات للمستخدم
    """

    # جلب جميع المدفوعات الخاصة بالمستخدم
    payments = add_payments.objects.filter(username=username)

    # البحث عن أول عملية دفع نشطة للمستخدم (التي حالتها "active")
    active_payment = payments.filter(status="active").first()

    # إذا لم يكن هناك اشتراك نشط، نرجع None مع جميع المدفوعات
    if not active_payment:
        return None, payments

    current_date = datetime.now().date()  # الحصول على التاريخ الحالي
    status_info = None  # متغير لتخزين بيانات الاشتراك النشط

    # التحقق من نوع الباقة
    if active_payment.package == "free":
        # إذا كانت الباقة مجانية، نتحقق من عدد الطلبات المتبقية
        if active_payment.numbercemande == 0:
            # إذا انتهت الطلبات المجانية، يتم إنهاء الاشتراك
            active_payment.status = "completed"
            active_payment.save()
        else:
            # إذا بقيت طلبات، يتم إرجاع عدد الطلبات المتبقية
            status_info = {
                'type': 'free',
                'remaining_orders': active_payment.numbercemande,
            }

    elif active_payment.package in ["advanced", "legendary"]:
        # إذا كانت الباقة متقدمة أو أسطورية، نتحقق من تاريخ الانتهاء
        if active_payment.end_date < current_date:
            # إذا انتهت صلاحية الاشتراك، يتم تحديث حالته إلى "completed"
            active_payment.status = "completed"
            active_payment.save()
        else:
            # إذا كان الاشتراك لا يزال نشطًا، نرجع تاريخ انتهائه
            status_info = {
                'type': active_payment.package,
                'end_date': active_payment.end_date,
            }

    return status_info, payments  # إرجاع بيانات الاشتراك النشط وقائمة جميع المدفوعات


def subscriptions(request):
    """ 
    دالة تعرض صفحة الاشتراكات 
    
    - تستدعي دالة `get_active_payment_status` لجلب حالة الاشتراك النشط.
    - تجمع جميع بيانات المدفوعات للمستخدم.
    - ترسل البيانات إلى القالب لعرضها في الواجهة الأمامية.
    
    :param request: كائن الطلب من Django
    :return: صفحة HTML تحتوي على بيانات الاشتراك
    """

    # استخراج اسم المستخدم الحالي من الجلسة
    current_username = request.user.username

    # استدعاء دالة get_active_payment_status للحصول على حالة الاشتراك والمدفوعات
    active_payment_status, payments = get_active_payment_status(current_username)

    # إعداد البيانات لتمريرها إلى القالب
    context = {
        'payments': payments,  # جميع عمليات الدفع الخاصة بالمستخدم
        'active_payment': active_payment_status,  # بيانات الاشتراك النشط (إذا وجد)
        'message': None,  # يمكن استخدامه لإرسال رسائل إلى الواجهة
        'error': None,  # يمكن استخدامه لإرسال أخطاء إلى الواجهة
    }

    # تمرير البيانات إلى قالب HTML لعرضها
    return render(request, 'payment/payment1.html', context)















from sweet_shared.models import sahlaboost
def serial_sahlaboost(request):
    message = ''
    if request.method == 'POST':
        form = sahlaboostForm(request.POST)
        if form.is_valid():
            conferm_serial = form.cleaned_data['conferm_serial']
            name_desktop = form.cleaned_data['name_desktop']
            
            # التحقق مما إذا كانت القيمة في name_desktop موجودة بالفعل في قاعدة البيانات
            name_desktop_instances = sahlaboost.objects.filter(name_desktop=name_desktop)
            if name_desktop_instances.exists():
                message = 'تم التأكد، يمكنك تسجيل الدخول بنجاح'
            else:

 # التحقق مما إذا كانت القيمة في conferm_serial موجودة بالفعل في قاعدة البيانات
                conferm_serial_instances = sahlaboost.objects.filter(conferm_serial=conferm_serial)
                if conferm_serial_instances.exists():
                  message = 'السيريال التأكيدي تم حجزه من قبل.'
                else:


                # البحث في حقل serial باستخدام القيمة المدخلة في conferm_serial
                  sahlaboost_instances = sahlaboost.objects.filter(serial=conferm_serial)
                  if sahlaboost_instances.exists():
                      sahlaboost_instance = sahlaboost_instances.first()
                      if sahlaboost_instance.serial == conferm_serial:
                          sahlaboost_instance.conferm_serial = conferm_serial
                          sahlaboost_instance.name_desktop = name_desktop
                          sahlaboost_instance.save()
                          message = 'تم الحفظ بنجاح'
                      else:
                          message = 'السيريال التأكيدي غير صحيح.'
                  else:
                      message = 'السيريال التأكيدي غير موجود في قاعدة البيانات.'




    else:
        form = sahlaboostForm()
    
    return render(request, 'serial_sahlaboost.html', {'form': form, 'message': message})