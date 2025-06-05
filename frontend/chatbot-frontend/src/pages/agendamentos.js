import React from 'react';
import CardMessage from '../components/cards/cardMessage';
import OffCanvas from '../components/menu/offcanvas.js'; // ajuste o caminho se estiver diferente
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function Agendamentos() {
    return (
        <div className="container py-5 ">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h2 className="fw-bold mb-0">Agendamentos</h2>
                <button
                    className="btn btn-success"
                    type="button"
                    data-bs-toggle="offcanvas"
                    data-bs-target="#offcanvasForm"
                    aria-controls="offcanvasForm"
                >
                    <i className="bi bi-plus-circle me-2"></i> Novo Agendamento
                </button>
            </div>

            <div className="row g-4">
                <CardMessage />
                <CardMessage />
                <CardMessage />
            </div>

            {/* OffCanvas */}
            <OffCanvas />
        </div>
    );
}

export default Agendamentos;
