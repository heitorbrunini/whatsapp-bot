package com.whatsapp.bot.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;


/**
 * Entidade para agendamento de mensagens (compromissos).
 * Baseada na estrutura do CSV: contato; data; mensagem; enviada.
 */
@Entity
@Table(name = "appointments")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Appointment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    /**
     * Relacionamento com a entidade Contato.
     * Muitos agendamentos podem pertencer a um contato.
     */
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "contact_id")
    private Contact contact;

    /**
     * Data e hora para o envio da mensagem.
     */
    private LocalDateTime scheduleDate;

    /**
     * O conteúdo da mensagem a ser enviada.
     */
    private String message;

    /**
     * Flag para indicar se a mensagem já foi enviada.
     */
    private boolean sent = false; // Valor padrão é false

}