import React from 'react';

function OffCanvas() {
    return (
        <div className="offcanvas offcanvas-end" tabIndex="-1" id="offcanvasForm" aria-labelledby="offcanvasFormLabel">
            <div className="offcanvas-header">
                <h5 className="offcanvas-title" id="offcanvasFormLabel">Novo Agendamento</h5>
                <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Fechar"></button>
            </div>
            <div className="offcanvas-body">
                <form>
                    <div className="mb-3">
                        <label htmlFor="contato" className="form-label">Contato (WhatsApp)</label>
                        <input type="text" className="form-control" id="contato" placeholder="ex: 83912345678" />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="mensagem" className="form-label">Mensagem</label>
                        <textarea className="form-control" id="mensagem" rows="3" placeholder="Digite a mensagem aqui..." />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="data" className="form-label">Data e Hora</label>
                        <input type="datetime-local" className="form-control" id="data" />
                    </div>
                    <button type="submit" className="btn btn-success w-100">
                        <i className="bi bi-send"></i> Agendar
                    </button>
                </form>
            </div>
        </div>
    );
}

export default OffCanvas;
