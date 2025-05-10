import { Link, useNavigate } from "react-router-dom";  // Importation de useNavigate
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
    const navigate = useNavigate();  // Initialisation de useNavigate pour la redirection

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
          setError(err.response?.data?.error || "Une erreur s’est produite.");
      }
    };
  
    return (
      <div>
      {successUrl ? (
        <div className="text-center text-green-600">
          Login réussie ! Redirection vers :{" "}
          <a href={successUrl} className="underline text-blue-600">
            Dashboard
          </a>
        </div>
      ) : (
      
        <form className="flex flex-col gap-6" onSubmit={handleSubmit}>
            <div className="flex flex-col items-center gap-2 text-center">
                <h1 className="text-2xl font-bold">Login to your account</h1>
                <p className="text-sm text-gray-500">
                    Enter your email below to login to your account
                </p>
            </div>

            <div className="grid gap-6">
                <div className="grid gap-2">
                    <label htmlFor="email" className="text-sm font-medium">
                        Email
                    </label>
                    <input
                        name="username"
                        id="email"
                        type="text"
                        placeholder="example"
                        onChange={handleChange}
                        required
                        className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black"
                    />
                </div>

                <div className="grid gap-2">
                    <div className="flex items-center justify-between">
                        <label htmlFor="password" className="text-sm font-medium">
                            Password
                        </label>
                        <a href="#" className="text-sm text-blue-500 hover:underline">
                            Forgot your password?
                        </a>
                    </div>
                    <input
                        name="password"
                        id="password"
                        type="password"
                        onChange={handleChange}
                        required
                        className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black"
                    />
                </div>

                <button
                    type="submit"
                    className="w-full rounded-md bg-purple-500 px-4 py-2 text-sm font-medium text-white hover:bg-gray-800"
                >
                    Login
                </button>

                {error && <p className="text-red-500 text-center">{error}</p>}  {/* Afficher le message d'erreur */}

                <div className="relative text-center text-sm">
                    <span className="relative z-10 bg-white px-2 text-gray-500">
                        Or continue with
                    </span>
                    <div className="absolute inset-0 top-1/2 border-t border-gray-300" />
                </div>

                <button
                    type="button"
                    className="flex w-full items-center justify-center gap-2 rounded-md border border-gray-300 px-4 py-2 text-sm hover:bg-gray-100"
                >
                    <FaGithub className="h-5 w-5" />
                    Login with GitHub
                </button>
            </div>

            <div className="text-center text-sm">
                Don’t have an account?{" "}
                <Link to="/Signup" className="underline hover:text-blue-600">Sign up</Link>
            </div>
        </form>
        )}
        </div>
    );
}
