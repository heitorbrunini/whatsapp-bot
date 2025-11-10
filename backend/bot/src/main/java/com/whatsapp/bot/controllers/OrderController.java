package com.whatsapp.bot.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.whatsapp.bot.dto.OrderDTO;
import com.whatsapp.bot.entities.Order;
import com.whatsapp.bot.services.OrderService;

@RestController
@RequestMapping("/orders")
@CrossOrigin(origins = "*")
public class OrderController {

    @Autowired
    private OrderService service;

    @PostMapping
    public OrderDTO createOrder(@RequestBody Order order) {
        return service.save(order);
    }

    @GetMapping
    public List<OrderDTO> getAllOrders() {
        return service.findAll();
    }

    @GetMapping("/{id}")
    public OrderDTO getOrderById(@PathVariable Long id) {
        return service.findOne(id);
    }

    @PutMapping()
    public OrderDTO updateOrder(@RequestBody Order order) {
        
        return service.update(order);
    }

    @DeleteMapping("/{id}")
    public void deleteOrder(@PathVariable Long id) {
        service.remove(id);
    }
}
