import { LoginForm } from "./LoginForm";

export default function Signin() {
  return (
    <div className="grid min-h-screen lg:grid-cols-2">
      {/* Colonne de gauche : Formulaire */}
      <div className="flex flex-col justify-center p-6 lg:p-12">
        <div className="mx-auto w-full max-w-md">
          <a href="#" className="mb-6 flex items-center gap-2 font-medium">
            <div className="flex h-6 w-6 items-center justify-center rounded-md bg-black text-white">
              <span className="text-sm font-bold">A</span>
            </div>
            Sahla DZ.
          </a>
          <LoginForm />
        </div>
      </div>

      {/* Colonne de droite : Image */}
      <div className="relative hidden lg:block">
        <img
          src="../public/images/Login.jpg" // remplace ce chemin par celui de ton image
          alt="Login visual"
          className="absolute inset-0 p-6 mx-auto my-auto"
        />
      </div>
    </div>
  );
}
