import "./index.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Signin from "./components/Signin";
import Signup from "./components/Signup";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/Signin" element={<Signin />} />
        <Route path="/Signup" element={<Signup />} />
      </Routes>
    </Router>
  );
}

export default App;
