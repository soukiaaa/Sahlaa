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
        alert("Inscription réussie !");
      }
    } catch (err) {
      setError(err.response?.data?.error || "Une erreur s’est produite.");
    }
  };  

  return (
    <div className="max-w-md mx-auto p-6 bg-white shadow rounded-lg mt-10">
      <h2 className="text-2xl font-bold mb-4 text-center">Créer un compte</h2>
      {error && <p className="text-red-500 text-sm text-center mb-4">{error}</p>}
      
        <form className="space-y-4" onSubmit={handleSubmit}>
          <input
            name="name"
            type="text"
            placeholder="Nom"
            value={formData.name}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 rounded px-3 py-2"
          />
          <input
            name="domain"
            type="text"
            placeholder="Nom de domaine (ex: boutique1)"
            value={formData.domain}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 rounded px-3 py-2"
          />
          <input
            name="username"
            type="text"
            placeholder="Nom d'utilisateur"
            value={formData.username}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 rounded px-3 py-2"
          />
          <input
            name="password"
            type="password"
            placeholder="Mot de passe"
            value={formData.password}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 rounded px-3 py-2"
          />
          <input
            name="phonenumber"
            type="text"
            placeholder="Numéro de téléphone"
            value={formData.phonenumber}
            onChange={handleChange}
            required
            className="w-full border border-gray-300 rounded px-3 py-2"
          />
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
          >
            S'inscrire
          </button>
          <div className="text-center text-sm">
            Don’t have an account?{" "}
            <Link to="/Signin" className="underline hover:text-blue-600">Login</Link>
          </div>
        </form>
    </div>
  );
}
