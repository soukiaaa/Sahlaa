import { LoginForm } from "./LoginForm";

export default function Signin() {
  return (
    <div className="grid min-h-screen lg:grid-cols-2">
      {/* Colonne de gauche : Formulaire */}
      <div className="flex flex-col justify-center p-6 lg:p-12">
        <div className="mx-auto w-full max-w-md">
       
          <LoginForm />
        </div>
      </div>

      {/* Colonne de droite : Image */}
    <div className="relative hidden lg:block lg:order-first">
  <img
    src="../public/images/backgroundlogin2.jpg" // قم بتعديل هذا المسار حسب الصورة
    alt="Login visual"
    className="absolute inset-0 w-full h-full object-cover"
  />
</div>
    </div>
  );
}
