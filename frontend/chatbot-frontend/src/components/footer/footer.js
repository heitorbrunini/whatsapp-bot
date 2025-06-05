import React from 'react';

const Footer = () => {
    return (
        <footer class="bg-dark text-white text-center py-4 mt-auto">
            <div class="container">
                <p class="mb-2">© 2023 Delivery Service. Todos os direitos reservados.</p>
                <ul class="list-inline mb-0">
                    <li class="list-inline-item"><a class="text-white text-decoration-none" href="#">Privacidade</a></li>
                    <li class="list-inline-item"><a class="text-white text-decoration-none" href="#">Termos</a></li>
                    <li class="list-inline-item"><a class="text-white text-decoration-none" href="#">Suporte</a></li>
                </ul>
            </div>
        </footer>
    );
};

export default Footer;