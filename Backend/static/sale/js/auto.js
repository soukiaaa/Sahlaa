document.addEventListener("DOMContentLoaded", function() {
    var image = document.getElementById("img"); // تحديد عنصر الصورة
    var inputField = document.getElementById("id_url_image"); // تحديد عنصر الإدخال

    if (image && inputField) {
        function setImageSrc() {
            var src = image.getAttribute("src"); // الحصول على قيمة src كما هي
            if (src) {
                inputField.value = src; // تخزين الرابط في حقل الإدخال
            }
        }

        if (image.complete) {
            setImageSrc(); // إذا كانت الصورة محملة بالفعل، احفظ الرابط مباشرة
        } else {
            image.onload = setImageSrc; // انتظر تحميل الصورة ثم احفظ الرابط
        }
    }
});
