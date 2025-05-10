from django.contrib import admin

from sweet_shared.models import SweetType, confirmserial,video_formation, Typesofsubscriptionplan,activation_money_book, bankinformation,addpayments, price, Payments, Situation, SituationColis, coliinformation, wilayaa, Confirmerlidentite, domainn,sahlaboost,Link_chromedriver
# Register your models here.
 
#@admin.register(SweetType)

#class SweetTypeAdmin(admin.ModelAdmin):

  # list_display=('name',)

@admin.register(SweetType)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ['get_name']

    def get_name(self, obj):
        return obj.name

    get_name.short_description = 'Name'


@admin.register(confirmserial)
class ConfirmSerialAdmin(admin.ModelAdmin):
    list_display = ('username', 'serial', 'confirmserial')



admin.site.register(Typesofsubscriptionplan)    





class BankInformationAdmin(admin.ModelAdmin):
    list_display = ('bankname', 'nameandsurname', 'accountnumber', 'address', 'email')
    list_filter = ('bankname',)  # يمكنك تغيير الحقول هنا إذا كنت تريد تصفية حسب حقل معين
    search_fields = ('bankname', 'nameandsurname', 'accountnumber', 'email')  # الحقول التي يمكن البحث عنها
    list_per_page = 20  # عدد السجلات لكل صفحة في واجهة الإدارة

admin.site.register(bankinformation, BankInformationAdmin)




admin.site.register(Confirmerlidentite)
admin.site.register(wilayaa) 

admin.site.register(Link_chromedriver) 


admin.site.register(Situation) 
admin.site.register(SituationColis) 
admin.site.register(coliinformation) 




admin.site.register(sahlaboost)
admin.site.register(activation_money_book)

admin.site.register(domainn)

admin.site.register(video_formation)



admin.site.register(price)   

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('username', 'numberoforders', 'orderprice', 'paymenttype', 'demand', 'remainingprice', 'gift')
    list_filter = ('demand', 'gift', 'paymenttype')
    search_fields = ('username', 'numberoforders', 'orderprice')
    list_per_page = 20

admin.site.register(Payments, PaymentsAdmin)
 

class AddPaymentsAdmin(admin.ModelAdmin):
    list_display = ('username', 'numberpayments', 'numbercemande')
    search_fields = ('username',)
    list_filter = ('numberpayments', 'numbercemande')

admin.site.register(addpayments, AddPaymentsAdmin)





from django.contrib import admin
from .models import add_payments

from django.contrib import admin


from django.utils.html import format_html

from django.utils.html import format_html

@admin.register(add_payments)
class AddPaymentsAdmin(admin.ModelAdmin):
    # الحقول التي ستظهر في قائمة الإدارة
    list_display = (
        'id', 
        
        'username', 
        'numbercemande', 
        'package', 
        'payment_type', 
        'start_date', 
        'end_date', 
        'amount', 
        'status',
        'display_receipt',  # عرض الصورة مع النقر
    )
    
    # الحقول القابلة للتعديل مباشرة من قائمة الإدارة
    list_editable = ('status', 'start_date', 'end_date')

    # الحقول القابلة للبحث
    search_fields = ('username', 'user__username', 'package', 'status')

    # الفلاتر الجانبية
    list_filter = ('package', 'status', 'start_date', 'end_date')

    # الحقول القابلة للتعديل في صفحة التفاصيل
    fields = (
      
        'username', 
        'numbercemande', 
        'package', 
        'payment_type', 
        'upload_receipt', 
        'start_date', 
        'end_date', 
        'amount', 
        'status',
    )

    # إضافة أيقونات وإجراءات إضافية
    actions = ['mark_as_pending', 'mark_as_active', 'mark_as_completed', 'mark_as_rejected']

    # دالة لعرض الصورة مع رابط
    def display_receipt(self, obj):
        if obj.upload_receipt:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" style="height: 50px; width: auto;" /></a>',
                obj.upload_receipt.url,
                obj.upload_receipt.url
            )
        return "لا يوجد وصل"

    display_receipt.short_description = "الوصل المرفوع"

    # إجراءات مخصصة لتحديث الحالة
    def mark_as_pending(self, request, queryset):
        queryset.update(status='pending')
        self.message_user(request, "تم تحديث الحالة إلى 'قيد مراجعة'.")

    def mark_as_active(self, request, queryset):
        queryset.update(status='active')
        self.message_user(request, "تم تحديث الحالة إلى 'نشطة'.")

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, "تم تحديث الحالة إلى 'مكتملة'.")

    def mark_as_rejected(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, "تم تحديث الحالة إلى 'رفض'.")

    # توصيف الإجراءات
    mark_as_pending.short_description = "تحديث الحالة إلى 'قيد مراجعة'"
    mark_as_active.short_description = "تحديث الحالة إلى 'نشطة'"
    mark_as_completed.short_description = "تحديث الحالة إلى 'مكتملة'"
    mark_as_rejected.short_description = "تحديث الحالة إلى 'رفض'"
