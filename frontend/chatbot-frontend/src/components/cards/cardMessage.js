import React from 'react';

const CardMessage = () => {
    return (

        <div class="col-md-6 col-lg-4">
            <div class="card agenda-card border-success shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">Contato: João</h5>
                    <p class="card-text">Mensagem: Pedido confirmado!</p>
                    <p class="card-text"><small class="text-muted">Data: 22/05/2025 15:00</small></p>
                    <span class="badge bg-success status-badge">Enviado</span>
                </div>
            </div>
        </div>

    );
};

export default CardMessage;