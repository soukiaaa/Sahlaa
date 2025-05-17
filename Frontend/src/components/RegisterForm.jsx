import React, { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";







export default function RegisterForm() {
  const [formData, setFormData] = useState({
    name: "",
    domain: "",
    username: "",
    password: "",
    phonenumber: "",
  });



  // هنا تضع دالة الفلترة مباشرة داخل المكون
  function normalizeDomainInput(value) {

    let val = value.replace(/\s+/g, ''); // إزالة الفراغات
    val = val.replace(/[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]/g, '');
    val = val.toLowerCase();              // تحويل إلى حروف صغيرة
    val = val.normalize('NFD').replace(/[\u0300-\u036f]/g, ''); // إزالة علامات التشكيل
    val = val.replace(/[^a-z]/g, '');    // السماح بحروف a-z فقط
    return val;
  }






  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };








  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      const response = await axios.post("http://localhost:8000/api/signup/", formData);
      if (response.data.redirect) {
        setTimeout(() => navigate("/Signin"), 2000);
        alert("تم التسجيل بنجاح!");
      }
    } catch (err) {
      setError(err.response?.data?.error || "حدث خطأ ما.");
    }
  };






  return (
    <div className="max-w-md mx-auto p-6 bg-white shadow rounded-lg mt-10" style={{ fontFamily: 'Cairo, sans-serif' }}>
      <h2 className="text-2xl font-bold mb-4 text-center">إنشاء حساب</h2>
      {error && <p className="text-red-500 text-sm text-center mb-4">{error}</p>}
      
<form className="space-y-4" onSubmit={handleSubmit}>
<input
  name="name"
  type="text"
  placeholder="الاسم الكامل"
  value={formData.name}
  onChange={(e) => {
    const onlyAllowed = e.target.value
      .toLowerCase() // تحويل كل شيء إلى أحرف صغيرة
      .replace(/[^a-z\u0621-\u064A\u067E\u0686\u0698\u06AF ]/g, ''); // إزالة الأرقام والرموز

    setFormData({ ...formData, name: onlyAllowed });
  }}
  required
  className="w-full border border-gray-300 rounded px-3 py-2 text-right"
  style={{ textTransform: 'lowercase' }} // للعرض فقط، القيمة يتم تعديلها من onChange
  title="يُسمح فقط بإدخال الأحرف العربية أو الأحرف الإنجليزية مع المسافات. يُمنع استخدام الأرقام أو الرموز."
/>



<input
  name="phonenumber"
  type="text"
  placeholder="رقم الهاتف"
  value={formData.phonenumber}
  onChange={(e) => {
    // السماح فقط بالأرقام
    const onlyNumbers = e.target.value.replace(/[^0-9]/g, '');
    
    // التأكد أن الطول لا يزيد عن 10
    if (onlyNumbers.length <= 10) {
      setFormData({ ...formData, phonenumber: onlyNumbers });
    }
  }}
  required
  maxLength="10"
  className="w-full border border-gray-300 rounded px-3 py-2 text-right"
  pattern="0[0-9]{9}"
  title="رقم الهاتف يجب أن يبدأ بـ 0 ويتكون من 10 أرقام فقط"
/>


<input
  name="username"
  type="text"
  placeholder="اسم المستخدم"
  value={formData.username}
  onChange={(e) => {
    const lowercase = e.target.value.toLowerCase();
    const onlyLetters = lowercase.replace(/[^a-z]/g, '');
    setFormData({ ...formData, username: onlyLetters });
  }}
  required
  className="w-full border border-gray-300 rounded px-3 py-2 text-right"
/>

<input
  name="password"
  type="password"
  placeholder="كلمة المرور"
  value={formData.password}
  onChange={(e) => {
    const value = e.target.value;
    // يمنع الحروف العربية والمسافات فقط
    const filtered = value.replace(/[\u0600-\u06FF\s]/g, '');
    handleChange({
      target: {
        name: 'password',
        value: filtered,
      },
    });
  }}
  required
  pattern="^[^\u0600-\u06FF\s]+$"
  title="كلمة المرور لا يجب أن تحتوي على حروف عربية أو فراغات."
  className="w-full border border-gray-300 rounded px-3 py-2 text-right"
/>

<input
  name="domain"
  type="text"
  placeholder="ادخل اسم الموقع"
  value={formData.domain}
  onChange={(e) => {
    const filteredValue = normalizeDomainInput(e.target.value);
    setFormData({ ...formData, domain: filteredValue });
  }}
  required
  className="w-full border border-gray-300 rounded px-3 py-2 text-right"
/>

  <button
    type="submit"
    className="w-full bg-[#1e1e1e] text-white py-2 rounded hover:bg-gray-900"
  >
    إنشاء الحساب
  </button>
  <div className="text-center text-sm">
    لديك حساب بالفعل؟{" "}
    <Link to="/Signin" className="underline hover:text-blue-600">
      تسجيل الدخول
    </Link>
  </div>
</form>

    </div>
  );
}
