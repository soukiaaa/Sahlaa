import { Link, useNavigate } from "react-router-dom";
import { FaGithub } from "react-icons/fa";
import axios from "axios";
import { useState } from "react";

export function LoginForm() {
    const [formData, setFormData] = useState({
        username: "",
        password: "",
    });

    const [error, setError] = useState(null);
    const [successUrl, setSuccessUrl] = useState(null);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        try {
            const response = await axios.post("http://localhost:8000/api/signin/", formData);
            setSuccessUrl(response.data.redirect);
        } catch (err) {
            setError(err.response?.data?.error || "حدث خطأ أثناء تسجيل الدخول.");
        }
    };

    return (
        <div dir="rtl" className="font-[Cairo]">
            {successUrl ? (
                <div className="text-center text-green-600">
                    تم تسجيل الدخول بنجاح! سيتم التوجيه إلى:{" "}
                    <a href={successUrl} className="underline text-blue-600">
                        لوحة التحكم
                    </a>
                </div>
            ) : (
                <form className="flex flex-col gap-6" onSubmit={handleSubmit}>
                    <div className="flex flex-col items-center gap-2 text-center">
                        <h1 className="text-2xl font-bold">تسجيل الدخول إلى حسابك</h1>
                        <p className="text-sm text-gray-500">
                            أدخل  اسم المستخدم وكلمة السر لتسجيل الدخول
                        </p>
                    </div>

                    <div className="grid gap-6">
                        <div className="grid gap-2">
                            <label htmlFor="email" className="text-sm font-medium">
إسم المستخدم                            </label>
<input
  name="username"
  id="email"
  type="text"
  placeholder="ادخل اسم المستخدم"
  value={formData.username}
  onChange={(e) => {
    const lowercase = e.target.value.toLowerCase();
    const onlyLetters = lowercase.replace(/[^a-z]/g, '');
    setFormData({ ...formData, username: onlyLetters });
  }}
  required
  className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black"
/>

                        </div>

                        <div className="grid gap-2">
                            <div className="flex items-center justify-between">
                                <label htmlFor="password" className="text-sm font-medium">
                                    كلمة المرور
                                </label>
                                <a href="#" className="text-sm text-blue-500 hover:underline">
                                    نسيت كلمة المرور؟
                                </a>
                            </div>
<input
  name="password"
  id="password"
  type="password"
  value={formData.password}   // لازم تربط القيمة بالحالة عشان التحديث يكون متحكم فيه
  onChange={(e) => {
    const value = e.target.value;
    // حذف الحروف العربية والمسافات
    const filtered = value.replace(/[\u0600-\u06FF\s]/g, '');
    setFormData({ ...formData, password: filtered });  // تحديث الحالة مباشرة مع القيمة المفلترة
  }}
  pattern="^[^\u0600-\u06FF\s]+$"
  title="كلمة المرور لا يجب أن تحتوي على حروف عربية أو فراغات."
  required
  className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black"
/>


                        </div>

                        <button
                            type="submit"
                            className="w-full rounded-md bg-[#1e1e1e] px-4 py-2 text-sm font-medium text-white hover:bg-gray-800"
                        >
                            تسجيل الدخول
                        </button>

                        {error && <p className="text-red-500 text-center">{error}</p>}

                  
                   
                    </div>

                    <div className="text-center text-sm">
                        ليس لديك حساب؟{" "}
                        <Link to="/Signup" className="underline hover:text-blue-600">سجل الآن</Link>
                    </div>
                </form>
            )}
        </div>
    );
}
