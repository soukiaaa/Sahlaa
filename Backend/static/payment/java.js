function changeTextTo512() {
    var numberOfOrdersInput = document.getElementById("id_numberoforders");
    var numberOfOrdersValue = parseInt(numberOfOrdersInput.value);
    
    var h5Text = document.getElementById("order");
    var h6Text = parseInt(h5Text.textContent);
    
    var totalElement = document.getElementById("total-price");
    totalElement.textContent = numberOfOrdersValue * h6Text;

    var remainingPriceInputElement = document.getElementById("id_remainingprice");
    remainingPriceInputElement.value = (numberOfOrdersValue * h6Text).toString();

    numberOfOrdersInput.addEventListener("input", changeTextTo512);
}

changeTextTo512();