from .models import Livraison

ALGERIAN_WILAYAS = [
    {'number': 1, 'name': 'أدرار'},
    {'number': 2, 'name': 'الشلف'},
    {'number': 3, 'name': 'الأغواط'},
    {'number': 4, 'name': 'أم البواقي'},
    {'number': 5, 'name': 'باتنة'},
    {'number': 6, 'name': 'بجاية'},
    {'number': 7, 'name': 'بسكرة'},
    {'number': 8, 'name': 'بشار'},
    {'number': 9, 'name': 'البليدة'},
    {'number': 10, 'name': 'البويرة'},
    {'number': 11, 'name': 'تمنراست'},
    {'number': 12, 'name': 'تبسة'},
    {'number': 13, 'name': 'تلمسان'},
    {'number': 14, 'name': 'تيارت'},
    {'number': 15, 'name': 'تيزي وزو'},
    {'number': 16, 'name': 'الجزائر'},
    {'number': 17, 'name': 'الجلفة'},
    {'number': 18, 'name': 'جيجل'},
    {'number': 19, 'name': 'سطيف'},
    {'number': 20, 'name': 'سعيدة'},
    {'number': 21, 'name': 'سكيكدة'},
    {'number': 22, 'name': 'سيدي بلعباس'},
    {'number': 23, 'name': 'عنابة'},
    {'number': 24, 'name': 'قالمة'},
    {'number': 25, 'name': 'قسنطينة'},
    {'number': 26, 'name': 'المدية'},
    {'number': 27, 'name': 'مستغانم'},
    {'number': 28, 'name': 'المسيلة'},
    {'number': 29, 'name': 'معسكر'},
    {'number': 30, 'name': 'ورقلة'},
    {'number': 31, 'name': 'وهران'},
    {'number': 32, 'name': 'البيض'},
    {'number': 33, 'name': 'إليزي'},
    {'number': 34, 'name': 'برج بوعريريج'},
    {'number': 35, 'name': 'بومرداس'},
    {'number': 36, 'name': 'الطارف'},
    {'number': 37, 'name': 'تندوف'},
    {'number': 38, 'name': 'تيسمسيلت'},
    {'number': 39, 'name': 'الوادي'},
    {'number': 40, 'name': 'خنشلة'},
    {'number': 41, 'name': 'سوق أهراس'},
    {'number': 42, 'name': 'تيبازة'},
    {'number': 43, 'name': 'ميلة'},
    {'number': 44, 'name': 'عين الدفلى'},
    {'number': 45, 'name': 'النعامة'},
    {'number': 46, 'name': 'عين تيموشنت'},
    {'number': 47, 'name': 'غرداية'},
    {'number': 48, 'name': 'غليزان'}
]


def populate_wilayas():
    for wilaya in ALGERIAN_WILAYAS:
        wilaia_name = f"{wilaya['number']} {wilaya['name']}"
        # التحقق مما إذا كانت الولاية موجودة بالفعل في قاعدة البيانات
        if not Livraison.objects.filter(wilaia=wilaia_name).exists():
            Livraison.objects.create(
                wilaia=wilaia_name,
                prix_livraison_domicile=0,
                prix_livraison_desktop=0
            )
    print("Wilayas have been populated successfully.")

# قم بتشغيل الدالة لتعبئة البيانات عند تشغيل السكربت
if __name__ == "__main__":
    populate_wilayas()
