import RegisterForm from "./RegisterForm";

export default function Signup() {
  return (
    <div className="grid min-h-screen lg:grid-cols-2">
      {/* Colonne de gauche : Formulaire */}
      <div className="flex flex-col justify-center p-6 lg:p-12">
        <div className="mx-auto w-full max-w-md">
     
          <RegisterForm />
        </div>
      </div>

      {/* Colonne de droite : Image */}
<div className="relative hidden lg:block lg:order-first w-full h-full">
  <img
    src="../public/images/backgroundlogin2.jpg"
    alt="Login visual"
    className="absolute top-0 left-0 w-full h-full object-cover"
  />
</div>

    </div>
  );
}
