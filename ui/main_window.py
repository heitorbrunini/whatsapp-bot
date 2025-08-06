from PyQt5.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget

from ui.chatbot_tab import setup_chatbot_page
from ui.orders_tab import setup_orders_page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bot_thread = None  
        self.setWindowTitle("Ilanax Delivery Admin")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # Páginas
        self.chatbot_page = QWidget()
        self.orders_page = QWidget()

        self.tabs.addTab(self.chatbot_page, "Chatbot")
        self.tabs.addTab(self.orders_page, "Pedidos")

        # Setup das páginas com retorno das funções de ação
        self.adicionar_log = setup_chatbot_page(self.chatbot_page, self)
        self.adicionar_pedido = setup_orders_page(self.orders_page)