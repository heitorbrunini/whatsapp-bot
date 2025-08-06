package com.whatsapp.bot.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.whatsapp.bot.entities.Order;

public interface OrderRepository extends JpaRepository<Order,Long> {

}
