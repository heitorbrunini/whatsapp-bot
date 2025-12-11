package com.whatsapp.bot.services;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import com.whatsapp.bot.dto.OrderDTO;
import com.whatsapp.bot.entities.Order;
import com.whatsapp.bot.repositories.OrderRepository;

class OrderServiceTest {

    @Mock
    private OrderRepository orderRepository;

    @InjectMocks
    private OrderService orderService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    @DisplayName("Deve salvar um pedido e retornar DTO correspondente")
    void testSaveOrder() {
        Order order = new Order();
        order.setId(1L);
        order.setClientName("Maria Silva");
        order.setAddress("Rua A, 123");
        order.setPaymentMethod("PIX");
        order.setObservations("Sem cebola");

        when(orderRepository.save(any(Order.class))).thenReturn(order);

        OrderDTO result = orderService.save(order);

        assertNotNull(result);
        assertEquals(order.getId(), result.id());
        assertEquals(order.getClientName(), result.clientName());
        verify(orderRepository, times(1)).save(order);
    }

    @Test
    @DisplayName("Deve listar todos os pedidos existentes")
    void testFindAllOrders() {
        Order o1 = new Order();
        o1.setId(1L);
        o1.setClientName("João");

        Order o2 = new Order();
        o2.setId(2L);
        o2.setClientName("Ana");

        when(orderRepository.findAll()).thenReturn(Arrays.asList(o1, o2));

        List<OrderDTO> result = orderService.findAll();

        assertEquals(2, result.size());
        assertEquals("João", result.get(0).clientName());
        verify(orderRepository, times(1)).findAll();
    }

    @Test
    @DisplayName("Deve buscar um pedido existente por ID")
    void testFindOneOrder() {
        Order order = new Order();
        order.setId(5L);
        order.setClientName("Carlos");

        when(orderRepository.findById(5L)).thenReturn(Optional.of(order));

        OrderDTO dto = orderService.findOne(5L);

        assertNotNull(dto);
        assertEquals("Carlos", dto.clientName());
        verify(orderRepository, times(1)).findById(5L);
    }

    @Test
    @DisplayName("Deve atualizar um pedido existente")
    void testUpdateOrder() {
        Order order = new Order();
        order.setId(10L);
        order.setClientName("Pedro");
        order.setAddress("Rua 1");
        order.setPaymentMethod("Cartão");
        order.setObservations("Nenhuma");

        Order dto = new Order(10L, "Paulo", "Rua Nova", "PIX", "Com gelo", null);

        when(orderRepository.findById(10L)).thenReturn(Optional.of(order));
        when(orderRepository.saveAndFlush(any(Order.class))).thenReturn(order);

        OrderDTO updated = orderService.update(dto);

        assertNotNull(updated);
        assertEquals("Paulo", updated.clientName());
        assertEquals("PIX", updated.paymentMethod());
        verify(orderRepository, times(1)).saveAndFlush(order);
    }

    @Test
    @DisplayName("Deve deletar um pedido existente")
    void testDeleteOrder() {
        Order order = new Order();
        order.setId(99L);
        order.setClientName("Lucas");

        when(orderRepository.findById(99L)).thenReturn(Optional.of(order));
        doNothing().when(orderRepository).deleteById(99L);

        orderService.remove(order);

        verify(orderRepository, times(1)).deleteById(99L);
    }
}
