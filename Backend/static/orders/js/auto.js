function updateSelectColor(selectElement) {
    let selectedValue = selectElement.value;

    // تعيين الألوان بناءً على الحالة المختارة
    let colors = {
        "new": "#9b59b6",       // جديد - بنفسجي
        "pending": "#f1c40f",   // قيد التأكيد - أصفر
        "call_1": "#f1c40f",    // الاتصال مرة - أصفر
        "call_2": "#f1c40f",    // الاتصال مرتين - أصفر
        "call_3": "#f1c40f",    // الاتصال ثلاث مرات - أصفر
        "confirmed": "#1abc9c", // مؤكدة - تركواز
        "delivery": "#3498db",  // شركة التوصيل - أزرق
        "completed": "#2ecc71", // مكتملة - أخضر
        "all": "#34495e",       // الكل - رمادي غامق
        "canceled": "#db545a"   // ملغي - أحمر
    };

    // تغيير لون الخلفية بناءً على الحالة المختارة
    selectElement.style.backgroundColor = colors[selectedValue] || "#ffffff"; // اللون الافتراضي أبيض
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("select[name='new_statut']").forEach(select => {
        updateSelectColor(select); // ضبط اللون عند تحميل الصفحة

        select.addEventListener("change", function() {
            updateSelectColor(this); // تحديث اللون عند تغيير الخيار
        });

        select.addEventListener("focus", function() {
            this.style.backgroundColor = "#ffffff"; // عند فتح القائمة، تصبح الخلفية بيضاء
        });

        select.addEventListener("blur", function() {
            updateSelectColor(this); // بعد اختيار الخيار، يعود اللون المناسب
        });
    });
});
