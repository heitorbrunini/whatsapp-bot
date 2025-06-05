import React from 'react';

const CardProduct = () => {
    return (
        <div class="col-sm-6 col-lg-3">
            <div class="card h-100 shadow-sm border-0">
                <img src="https://image.gobox.app.br/produto/219/t11002.png?v=1" class="card-img-top" alt="Pedido"></img>
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <h5 class="card-title mb-0">Pedido #001</h5>
                        <span class="badge bg-warning text-dark status-badge">Em produção</span>
                    </div>
                    <p class="card-text text-muted">Pizza Calabresa, Coca 2L</p>
                    <div class="dropdown">
                        <button class="btn btn-outline-primary w-100 dropdown-toggle" type="button" data-bs-toggle="dropdown">
                            <i class="bi bi-arrow-repeat me-1"></i> Atualizar Status
                        </button>
                        <ul class="dropdown-menu w-100">
                            <li><a class="dropdown-item" href="#"><i class="bi bi-truck"></i> Rota de Entrega</a></li>
                            <li><a class="dropdown-item" href="#"><i class="bi bi-gear-fill"></i> Em produção</a></li>
                            <li><a class="dropdown-item" href="#"><i class="bi bi-check-circle"></i> Aceito</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CardProduct;