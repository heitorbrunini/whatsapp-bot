package com.whatsapp.bot.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.whatsapp.bot.entities.OrderItem;

public interface OrderItemRepository extends JpaRepository<OrderItem, Long>{

}
