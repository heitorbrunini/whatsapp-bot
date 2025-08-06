package com.whatsapp.bot.dto;

import com.whatsapp.bot.entities.Order;
import java.util.List;

/**
 * DTO para representar um pedido completo com seus itens.
 */
public record OrderDTO(
        Long id,
        String clientName,
        String address,
        String paymentMethod,
        String observations,
        List<OrderItemDTO> items
) {
    public OrderDTO(Order entity) {
        this(
                entity.getId(),
                entity.getClientName(),
                entity.getAddress(),
                entity.getPaymentMethod(),
                entity.getObservations(),
                // Converte a lista de entidades OrderItem para uma lista de OrderItemDTO
                entity.getItems().stream().map(OrderItemDTO::new).toList()
        );
    }
}