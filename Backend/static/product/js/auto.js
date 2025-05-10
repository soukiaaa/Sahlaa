document.addEventListener("DOMContentLoaded", function() {
    // استخراج السعر من عنصر <h5>
    let priceElement = document.querySelector(".u-text-2");
    let priceInput = document.getElementById("id_prix_Total_a_ramasser");

    if (priceElement && priceInput) {
        // استخراج الرقم من النص (مع إزالة " DA")
        let priceText = priceElement.textContent.trim();
        let priceValue = parseFloat(priceText.replace(" DA", "").trim());

        // التحقق من أن القيمة رقمية قبل وضعها في الـ input
        if (!isNaN(priceValue)) {
            priceInput.value = priceValue;
        }
    }
});