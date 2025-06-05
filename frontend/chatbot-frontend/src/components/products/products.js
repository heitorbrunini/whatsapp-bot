import React from 'react';
import CardProduct from '../cards/cardProduct';
const Products = () => {
    return (
        <div class="container py-5">
            <div class="text-center mb-5">
                <h2 class="fw-bold">Acompanhamento de Pedidos</h2>
                <p class="text-muted">Gerencie os pedidos e controle o status de forma integrada ao chatbot.</p>
            </div>

            <div class="row g-4">
                <CardProduct/>
                <CardProduct/>
                <CardProduct/>
                <CardProduct/>
            </div>
        </div>
    );
};


export default Products;