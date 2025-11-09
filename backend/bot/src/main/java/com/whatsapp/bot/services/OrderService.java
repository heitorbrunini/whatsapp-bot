package com.whatsapp.bot.services;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.whatsapp.bot.dto.OrderDTO;
import com.whatsapp.bot.entities.Order;
import com.whatsapp.bot.repositories.OrderRepository;

@Service
public class OrderService {
	
	@Autowired
	private OrderRepository repository;
	
	public OrderDTO save (Order order) {
		repository.save(order);
		return new OrderDTO(order);
	}
	
	public List<OrderDTO> findAll(){
		List<OrderDTO> dtos = new ArrayList<>();
		List<Order> data = repository.findAll();
		
		data.forEach(ord -> dtos.add(new OrderDTO (ord)));
		
		return dtos;
	}
	
	public void remove(Order dto) {
		repository.deleteById(dto.getId());
	}
	
	public OrderDTO findOne(Long id) {
		return new OrderDTO (repository.findById(id).get());
	}
	
	public OrderDTO update(OrderDTO dto) {
		
		Order data = repository.findById(dto.id()).get();
		
		data.setClientName(dto.clientName());
		data.setAddress(dto.address());
		data.setPaymentMethod(dto.paymentMethod());
		data.setObservations(dto.observations());
		
		repository.saveAndFlush(data);
		
		return new OrderDTO (data);
	}
	

}
