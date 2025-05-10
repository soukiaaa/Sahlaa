
function changeText() {
 // document.getElementById("bi").style.display = "none";

    document.getElementById("id_wilaya").style.color = "red";

    // الحصول على القيمة المحددة في حقل الولاية

   // var spanid = document.getElementById("id_wilaya").value;
  //  document.getElementById("cc").setAttribute("value", spanid);


   // var spani = document.getElementById("cc").setAttribute("value", spanid);
   // spani.style.color = "red";






  // document.getElementById("wilayaa_iddz").value = "constantine";
    
   
   document.getElementById("get_selected_text");
   var wilayaSelect = document.getElementById("id_wilaya");
   var selectedOption = wilayaSelect.options[wilayaSelect.selectedIndex];
   var selectedText = selectedOption.textContent;
  // alert("Selected Wilaya: " + selectedText);

   document.getElementById("wilayaa_iddz").value = selectedText;

   document.getElementById("getprix").click();
  
   //*********************** */

   
 // احصل على عنصر الاختيار باستخدام معرفه











  //*********************** */







// تأخير السكربت لمدة 2 ثانية (2000 مللي ثانية)
//setTimeout(function() {



// تحديد العنصر الذي يحمل الهوية "id_wilaya"
var wilayaSelect = document.getElementById("id_wilaya");

// تحديد القيمة التي تريد تحديدها (في هذه الحالة "constantine")
var selectedValue = "5";

// البحث عن الخيار الذي يحمل القيمة المحددة وتحديد الخيار
for (var i = 0; i < wilayaSelect.options.length; i++) {
  if (wilayaSelect.options[i].value === selectedValue) {
    wilayaSelect.options[i].selected = true;
    break;
  }
}


//}, 90000); // تعيين الوقت الذي تريد تأخيره بالمللي ثانية هنا







 }
 


 // تنفيذ الدالة عند تغيير قيمة حقل الولاية
 document.getElementById("id_wilaya").addEventListener("change", changeText);
// تنفيذ الدالة عند تحميل الصفحة
// document.addEventListener('DOMContentLoaded', changeText);
  


 





function change() {
    document.getElementById("ba").style.color = "red";

    var wilayaSelect = document.getElementById("id_wilaya");
    wilayaSelect.options[4].selected = true;


    
  var selectedValue = "5";

  for (var i = 0; i < wilayaSelect.options.length; i++) {
    if (wilayaSelect.options[i].value === selectedValue) {
      wilayaSelect.options[i].selected = true;
      break;
    }
  }





















}

document.getElementById("some_id1").addEventListener("click", change);














function changee() {

// احصل على عنصر الاختيار باستخدام معرفه
var selectElement = document.getElementById("id_livrioncoli");

// احصل على النص المحدد
var selectedText = selectElement.options[selectElement.selectedIndex].text;

// طباعة النص المحدد
console.log(selectedText);

 // تحقق إذا كانت القيمة المحددة تساوي "DOMICEL"
 if (selectedText === "DOMICEL") {
  // قم بتنفيذ الإجراء الذي ترغب فيه عند توافق القيمة
 
  document.getElementById("gg").style.display = "block";          
  document.getElementById("jj").style.display = "none";
 

var prixproduct =document.getElementById("id_prixproduct").value;
// احصل على العنصر باستخدام الهوية (ID)
var element = document.getElementById("gg");
// احصل على نص العنصر
var text = element.textContent || element.innerText;
// قم بإزالة أي أحرف غير رقمية من النص
var number = text.replace(/\D/g, '');
// قم بتحويل النص إلى رقم صحيح
var prixlivrision = parseInt(number);

// الآن يمكنك استخدام المتغير "numericValue" للعمل مع الرقم
console.log(prixlivrision);

var totalValue = parseInt(prixlivrision) + parseInt(prixproduct);

// تحديث النص في العنصر الذي له الهوية (ID) "total" بالقيمة الجديدة
document.getElementById("total").textContent = totalValue + ' DA';
 









}
 // تحقق إذا كانت القيمة المحددة تساوي "DOMICEL"
 if (selectedText === "STOPDESK") {
  // قم بتنفيذ الإجراء الذي ترغب فيه عند توافق القيمة
 
  document.getElementById("gg").style.display = "none";          
  document.getElementById("jj").style.display = "block";



  // يمكنك استبدال الإجراء المذكور بالإجراء الذي ترغب في تنفيذه.
  var prixproduct =document.getElementById("id_prixproduct").value;
  // احصل على العنصر باستخدام الهوية (ID)
  var element = document.getElementById("jj");
  // احصل على نص العنصر
  var text = element.textContent || element.innerText;
  // قم بإزالة أي أحرف غير رقمية من النص
  var number = text.replace(/\D/g, '');
  // قم بتحويل النص إلى رقم صحيح
  var prixlivrision = parseInt(number);

  // الآن يمكنك استخدام المتغير "numericValue" للعمل مع الرقم
  console.log(prixlivrision);

  var totalValue = parseInt(prixlivrision) + parseInt(prixproduct);

  // تحديث النص في العنصر الذي له الهوية (ID) "total" بالقيمة الجديدة
  document.getElementById("total").textContent = totalValue + ' DA';

}


}
document.addEventListener('DOMContentLoaded', changee);
document.getElementById("id_livrioncoli").addEventListener("click", changee);
document.getElementById("id_prixproduct").addEventListener("click", changee);