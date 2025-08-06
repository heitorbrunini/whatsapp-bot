package com.whatsapp.bot.entities;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import java.util.ArrayList;
import java.util.List;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

/**
 * Representa um pedido, contendo os dados do cliente e uma lista de itens.
 */
@Entity
// "order" é uma palavra reservada em SQL, por isso é uma boa prática
// nomear a tabela como "orders" ou "customer_orders".
@Table(name = "orders")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String clientName;

    private String address;

    private String paymentMethod;

    private String observations;

    @OneToMany(
            mappedBy = "order", // "order" é o nome do campo na classe OrderItem
            cascade = CascadeType.ALL, // Salva, atualiza e remove os itens junto com o pedido
            orphanRemoval = true, // Remove itens da lista que não têm mais um pedido associado
            fetch = FetchType.LAZY
    )
    private List<OrderItem> items = new ArrayList<>();

    // Métodos auxiliares para sincronizar o relacionamento (boa prática)
    public void addItem(OrderItem item) {
        items.add(item);
        item.setOrder(this);
    }

    public void removeItem(OrderItem item) {
        items.remove(item);
        item.setOrder(null);
    }
}