package com.whatsapp.bot.dto;

import com.whatsapp.bot.entities.OrderItem;
import java.math.BigDecimal;

/**
 * DTO para representar um item de um pedido.
 */
public record OrderItemDTO(
        Long id,
        String product,
        String size,
        int quantity,
        BigDecimal price
) {
    public OrderItemDTO(OrderItem entity) {
        this(
                entity.getId(),
                entity.getProduct(),
                entity.getSize(),
                entity.getQuantity(),
                entity.getPrice()
        );
    }
}