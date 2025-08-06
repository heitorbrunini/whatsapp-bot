from PyQt5.QtWidgets import (
    QVBoxLayout, QLabel, QScrollArea, QWidget, QGridLayout,
    QFrame, QComboBox
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

orders_layout = None
pedido_index = 0  # contador global de pedidos

def setup_orders_page(parent_widget):
    global orders_layout, pedido_index

    def calcular_posicao():
        row = pedido_index // 2
        col = pedido_index % 2
        return row, col

    def create_order_card(order_id, product_name):
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        card.setFrameShadow(QFrame.Raised)
        card_layout = QVBoxLayout(card)

        image_label = QLabel()
        pixmap = QPixmap(200, 150)
        pixmap.fill(Qt.lightGray)
        image_label.setPixmap(pixmap)
        card_layout.addWidget(image_label)

        order_label = QLabel(f"<b>Pedido #{order_id}</b>")
        order_label.setFont(QFont("Roboto", 12))
        order_label.setStyleSheet("color: #333;")
        card_layout.addWidget(order_label)

        product_label = QLabel(product_name)
        card_layout.addWidget(product_label)

        status_combo = QComboBox()
        status_combo.addItems(["Aceito", "Em Produção", "Rota", "Entregue"])
        status_combo.setFixedWidth(140)  # Largura fixa
        status_combo.setFixedHeight(30)  # Altura opcional
        status_combo.setStyleSheet("font-size: 12px; padding: 2px;")
        card_layout.addWidget(status_combo, alignment=Qt.AlignLeft)


        return card

    layout = QVBoxLayout(parent_widget)
    layout.setAlignment(Qt.AlignTop)

    title_label = QLabel("Acompanhamento de Pedidos")
    title_label.setFont(QFont("Roboto", 24, QFont.Bold))
    layout.addWidget(title_label, alignment=Qt.AlignCenter)

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    orders_container = QWidget()
    orders_layout = QGridLayout(orders_container)

    # Exemplo de pedidos (remova depois)
    adicionar_card_inicial = lambda id, desc: orders_layout.addWidget(
        create_order_card(id, desc), *calcular_posicao()
    )
    adicionar_card_inicial("001", "Pizza Calabresa, Coca-Cola 2L")
    pedido_index += 1
    adicionar_card_inicial("002", "Hambúrguer, Batata Frita")
    pedido_index += 1

    scroll_area.setWidget(orders_container)
    layout.addWidget(scroll_area)

    def adicionar_pedido(order_id, product_name):
        global pedido_index
        if orders_layout:
            row, col = calcular_posicao()
            orders_layout.addWidget(create_order_card(order_id, product_name), row, col)
            pedido_index += 1

    return adicionar_pedido
