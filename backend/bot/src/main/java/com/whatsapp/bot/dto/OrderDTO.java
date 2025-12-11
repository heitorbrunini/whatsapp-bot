package com.whatsapp.bot.dto;

import com.whatsapp.bot.entities.Order;
import java.util.List;

/**
 * DTO para representar um pedido completo com seus itens.
 */
import com.fasterxml.jackson.annotation.JsonProperty;

public record OrderDTO(
        Long id,

        @JsonProperty("cliente")
        String clientName,

        @JsonProperty("endereco")
        String address,

        @JsonProperty("forma_pagamento")
        String paymentMethod,

        @JsonProperty("observacoes")
        String observations,

        @JsonProperty("itens")
        List<OrderItemDTO> items
) {
    public OrderDTO(Order entity) {
        this(
                entity.getId(),
                entity.getClientName(),
                entity.getAddress(),
                entity.getPaymentMethod(),
                entity.getObservations(),
                entity.getItems().stream().map(OrderItemDTO::new).toList()
        );
    }
}
