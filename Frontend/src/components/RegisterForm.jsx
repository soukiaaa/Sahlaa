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
    onChange={handleChange}
    required
    className="w-full border border-gray-300 rounded px-3 py-2 text-right"
  />

<input
  name="phonenumber"
  type="text"
  placeholder="رقم الهاتف"
  value={formData.phonenumber}
  onChange={handleChange}
  required
  pattern="0[0-9]{9}"
  maxLength="10"
  className="w-full border border-gray-300 rounded px-3 py-2 text-right"
/>


  <input
    name="username"
    type="text"
    placeholder="اسم المستخدم"
    value={formData.username}
    onChange={handleChange}
    required
    className="w-full border border-gray-300 rounded px-3 py-2 text-right"
  />
  <input
    name="password"
    type="password"
    placeholder="كلمة المرور"
    value={formData.password}
    onChange={handleChange}
    required
    className="w-full border border-gray-300 rounded px-3 py-2 text-right"
  />
  <input
    name="domain"
    type="text"
    placeholder="ادخل اسم الموقع"
    value={formData.domain}
    onChange={handleChange}
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
