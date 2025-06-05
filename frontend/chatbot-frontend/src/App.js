import React, { useState } from 'react';
import Navbar from "./components/navbar/navbar.js";
import Orders from "./pages/orders.js";
import Chatbot from './pages/chatbot.js';
import Agendamentos from "./pages/agendamentos.js";
import Footer from "./components/footer/footer.js";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';

function App() {
  const [paginaAtual, setPaginaAtual] = useState("orders");

  return (
    <div className="App ">
      <div className="d-flex flex-column min-vh-100">
        <Navbar onNavigate={setPaginaAtual} />
        <div className=" bg-body-tertiary">
          {paginaAtual === "orders" && <Orders />}
          {paginaAtual === "agendamentos" && <Agendamentos />}
          {paginaAtual === "chatbot" && <Chatbot />}
        </div>


        <Footer />
      </div>
    </div>
  );
}

export default App;
