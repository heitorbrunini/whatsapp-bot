import React from 'react';

function Chatbot() {
    return (
        <div className="container py-5">
            {/* Título */}
            <div className="text-center mb-4">
                <h2 className="fw-bold">Controle do Chatbot</h2>
                <p className="text-muted">Gerencie a automação de mensagens no WhatsApp e visualize os logs em tempo real.</p>
            </div>

            {/* Botões de controle */}
            <div className="d-flex justify-content-center gap-3 mb-4">
                <button className="btn btn-success"><i className="bi bi-play-fill me-1"></i> Iniciar</button>
                <button className="btn btn-danger"><i className="bi bi-stop-fill me-1"></i> Parar</button>
                <button className="btn btn-warning"><i className="bi bi-arrow-repeat me-1"></i> Reiniciar</button>
            </div>

            {/* Área de Logs */}
            <div className="card bg-dark text-white shadow-sm">
                <div className="card-header border-bottom text-success">
                    <i className="bi bi-terminal me-2"></i> Logs do Bot
                </div>
                <div className="card-body" style={{ height: '400px', overflowY: 'auto', fontFamily: 'monospace', fontSize: '0.9rem' }}>
                    <p>[15:03:21] Bot iniciado com sucesso.</p>
                    <p>[15:03:25] Conectado ao WhatsApp Web.</p>
                    <p>[15:04:01] Nova mensagem recebida de (83912345678).</p>
                    <p>[15:04:05] Resposta enviada com sucesso.</p>
                    <p>[15:04:12] Aguardando novas mensagens...</p>
                    <p>[15:05:55] Mensagem agendada enviada.</p>
                    <p>[15:07:00] Sessão ativa.</p>
                    <p>[15:09:14] Bot pausado pelo usuário.</p>
                    <p>[15:10:01] Bot reiniciado.</p>
                </div>
            </div>
        </div>
    );
}

export default Chatbot;
