document.addEventListener("DOMContentLoaded", function () {
    // تحديد عناصر الراديو
    const radioButtons = document.querySelectorAll('input[name="package"]');
  
    // تحديد العناصر التي سيتم إخفاؤها
    const elementsToHide = [
        document.querySelector('.u-border-1.u-border-grey-dark-1.u-form-group.u-form-line'),
        document.querySelector('label[for="id_numbercemande"]'),
        document.querySelector('#id_numbercemande').closest('.u-input-row'),
        document.querySelector('.u-form-group.u-form-text.u-text-3'),
    ];

    // تحديد عناصر الأسعار
    const prix1 = document.getElementById("prix_1");
    const prix2 = document.getElementById("prix_2");
    const prix3 = document.getElementById("prix_3");

    // وظيفة للتحقق من الباقة المختارة وإظهار السعر المناسب
    function toggleElements() {
        const selectedPackage = document.querySelector('input[name="package"]:checked').value;

        // إخفاء جميع الأسعار في البداية
        prix1.style.display = "none";
        prix2.style.display = "none";
        prix3.style.display = "none";

        // إظهار السعر المناسب بناءً على الباقة المختارة
        if (selectedPackage === "advanced") {
            prix1.style.display = "inline";
            elementsToHide.forEach((el) => el.style.display = "none"); // إخفاء العناصر
        } else if (selectedPackage === "legendary") {
            prix2.style.display = "inline";
            elementsToHide.forEach((el) => el.style.display = "none"); // إخفاء العناصر
        } else {
            prix3.style.display = "inline";
            elementsToHide.forEach((el) => el.style.display = "flex"); // إظهار العناصر
        }
    }

    // استدعاء الوظيفة عند التحميل الأولي للصفحة
    toggleElements();

    // إضافة حدث التغيير لعناصر الراديو
    radioButtons.forEach((radio) => {
        radio.addEventListener("change", toggleElements);
    });
});



document.addEventListener("DOMContentLoaded", function () {
    // تحديد الحقول والعناصر المطلوبة
    const inputNumberCemande = document.getElementById("id_numbercemande");
    const orderPriceElement = document.querySelector(".order-price");
    const prix3Element = document.getElementById("prix_3");

    // التحقق من وجود السعر داخل العنصر
    const orderPrice = parseFloat(orderPriceElement.textContent.trim()) || 0;

    // وظيفة لحساب المجموع وتحديث العنصر prix_3
    function updateTotal() {
        const numberOfOrders = parseInt(inputNumberCemande.value.trim()) || 0;
        const total = numberOfOrders * orderPrice;

        // تحديث القيمة داخل العنصر prix_3 بدون أرقام عشرية
        prix3Element.textContent = Math.round(total); // عرض النتيجة كعدد صحيح
    }

    // إضافة حدث عند تغيير القيمة في حقل عدد الطلبيات
    inputNumberCemande.addEventListener("input", updateTotal);

    // استدعاء الوظيفة لتحديث المجموع عند التحميل الأولي
    updateTotal();
});




document.addEventListener("DOMContentLoaded", function () {
    const selectElement = document.getElementById("id_payment_type");
    const bankDetails = document.querySelectorAll(".u-group-4");

    selectElement.addEventListener("change", function() {
      const selectedBankId = selectElement.value;

      bankDetails.forEach(function(bankDiv) {
        const bankId = bankDiv.getAttribute("id");

        if (bankId === selectedBankId) {
          bankDiv.style.display = "block";  // إظهار البنك المحدد
        } else {
          bankDiv.style.display = "none";   // إخفاء البنوك الأخرى
        }
      });
    });

    // إخفاء جميع البنوك عند تحميل الصفحة باستثناء البنك الأول
    bankDetails.forEach(function(bankDiv, index) {
      if (index !== 0) {
        bankDiv.style.display = "none";  // إخفاء باقي البنوك
      }
    });
  });








  document.addEventListener("DOMContentLoaded", function () {
    // تحديد عناصر الراديو أو أي طريقة لاختيار الباقة
    const radioButtons = document.querySelectorAll('input[name="package"]');
    const amountInput = document.getElementById('id_amount');

    // وظيفة لحساب المجموع بناءً على السعر وعدد الطلبيات
    function calculateTotal() {
        let price = 0;

        // الحصول على السعر بناءً على الباقة المختارة
        if (document.getElementById('prix_1').style.display !== 'none') {
            price = parseFloat(document.querySelector('#prix_1 .order-price').textContent) || 0;
        } else if (document.getElementById('prix_2').style.display !== 'none') {
            price = parseFloat(document.querySelector('#prix_2 .order-price').textContent) || 0;
        } else if (document.getElementById('prix_3').style.display !== 'none') {
            price = parseFloat(document.querySelector('#prix_3').textContent) || 0;
        }

        const numberOfOrders = parseInt(document.querySelector('input[name="numbercemande"]').value, 10) || 0; // عدد الطلبيات

        // حساب المجموع
        const total = price * numberOfOrders;

        // إدخال المجموع في الـ input المخفي
        amountInput.value = total.toFixed(2); // التنسيق ليكون رقم عشري مع نقطتين
    }

    // إضافة حدث عند تغيير عدد الطلبيات
    document.querySelector('input[name="numbercemande"]').addEventListener('input', calculateTotal);

    // إضافة حدث عند تغيير الباقة المختارة
    radioButtons.forEach((radio) => {
        radio.addEventListener("change", calculateTotal);
    });

    // استدعاء الدالة في البداية لحساب المجموع عند تحميل الصفحة
    calculateTotal();
});

