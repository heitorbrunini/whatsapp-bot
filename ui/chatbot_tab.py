import os
import sys
from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QScrollArea, QWidget
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from bot.scripts.worker_bot import BotWorker  # Certifique-se de que o caminho esteja correto

log_box_layout = None
log_scroll_area = None

def setup_chatbot_page(parent_widget, main_window):
    global log_box_layout, log_scroll_area    

    layout = QVBoxLayout(parent_widget)
    layout.setAlignment(Qt.AlignCenter)

    title_label = QLabel("Logs do Bot")
    title_label.setFont(QFont("Roboto", 24, QFont.Bold))
    layout.addWidget(title_label, alignment=Qt.AlignCenter)

    controls_frame = QFrame()
    controls_layout = QHBoxLayout(controls_frame)
    controls_layout.setAlignment(Qt.AlignCenter)

    start_button = QPushButton("Iniciar")
    start_button.setStyleSheet("background-color: #4CAF50; color: white;")
    stop_button = QPushButton("Parar")
    stop_button.setStyleSheet("background-color: #F44336; color: white;")
    restart_button = QPushButton("Reiniciar")
    restart_button.setStyleSheet("background-color: #FFC107; color: black;")

    controls_layout.addWidget(start_button)
    controls_layout.addWidget(stop_button)
    controls_layout.addWidget(restart_button)
    layout.addWidget(controls_frame)

    # Área de logs com scroll
    log_scroll_area = QScrollArea()
    log_scroll_area.setWidgetResizable(True)
    log_content = QWidget()
    log_content_layout = QVBoxLayout(log_content)
    log_content_layout.setAlignment(Qt.AlignTop)

    # Título da área de log
    log_label_title = QLabel("🧠 Logs do sistema")
    log_label_title.setFont(QFont("Roboto", 12, QFont.Bold))
    log_content_layout.addWidget(log_label_title)

    # Caixinha onde os logs irão aparecer
    log_frame = QWidget()
    log_box_layout = QVBoxLayout(log_frame)
    log_box_layout.setAlignment(Qt.AlignTop)
    log_box_layout.setSpacing(5)

    # Mensagem inicial
    initial_log = QLabel("Os logs em tempo real serão exibidos aqui...")
    initial_log.setStyleSheet("padding: 5px; color: gray;")
    log_box_layout.addWidget(initial_log)

    log_frame.setStyleSheet("border: 1px solid #ccc; background-color: #f9f9f9; padding: 5px;")

    log_scroll_area.setWidget(log_frame)
    layout.addWidget(log_scroll_area)

    def adicionar_log(mensagem: str):
        global log_box_layout, log_scroll_area
        if log_box_layout:
            novo_log = QLabel(mensagem)
            novo_log.setStyleSheet("padding: 5px;")
            log_box_layout.addWidget(novo_log)
            log_scroll_area.verticalScrollBar().setValue(
                log_scroll_area.verticalScrollBar().maximum()
            )

    def iniciar_bot():
        if not main_window.bot_thread:
            main_window.bot_thread = BotWorker()
            main_window.bot_thread.nova_mensagem_log.connect(main_window.adicionar_log)
            main_window.bot_thread.novo_pedido.connect(main_window.adicionar_pedido)
            main_window.bot_thread.start()
            main_window.bot_thread.start_bot_loop()
            adicionar_log("[LOG] Bot iniciado.")
        elif not main_window.bot_thread.running:
            main_window.bot_thread.start_bot_loop()
            adicionar_log("[LOG] Bot reiniciado.")
        else:
            adicionar_log("[AVISO] Bot já está em execução.")

    def parar_bot():
        if main_window.bot_thread and main_window.bot_thread.running:
            main_window.bot_thread.stop_bot_loop()
            adicionar_log("[LOG] Bot parado.")
        else:
            adicionar_log("[AVISO] Nenhum bot em execução.")


    def reiniciar_tudo():
        adicionar_log("[INFO] Reiniciando a aplicação...")
        main_window.bot_thread.close_driver()
        main_window.close()

        # Caminho raiz do projeto
        projeto_path = r"D:\Programas\PYTHON\whatsapp-bot"

        # Altera para o diretório correto
        os.chdir(projeto_path)

        # Caminho absoluto do arquivo principal
        caminho_app_py = os.path.join(projeto_path, "app.py")

        # Reinicia o processo
        python = sys.executable
        os.execl(python, python, caminho_app_py)


    start_button.clicked.connect(iniciar_bot)
    stop_button.clicked.connect(parar_bot)
    restart_button.clicked.connect(reiniciar_tudo)

    return adicionar_log