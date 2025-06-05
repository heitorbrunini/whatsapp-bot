import React from 'react';

const Navbar = ({ onNavigate }) => {
  return (
    <nav className="navbar navbar-expand-lg bg-dark navbar-dark">
      <div className="container">
        <a className="navbar-brand fw-bold" href="#">
          <i className="bi bi-shop"></i> Ilanax Delivery
        </a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <button className="nav-link btn btn-link text-white" onClick={() => onNavigate("orders")}>
                Pedidos
              </button>
            </li>
            <li className="nav-item">
              <button className="nav-link btn btn-link text-white" onClick={() => onNavigate("agendamentos")}>
                Agendamentos
              </button>
            </li>
            <li className="nav-item">
              <button className="nav-link btn btn-link text-white" onClick={() => onNavigate("chatbot")}>
                Chatbot
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
