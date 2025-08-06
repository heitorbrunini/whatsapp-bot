package com.whatsapp.bot.dto;

import com.whatsapp.bot.entities.Appointment;
import java.time.LocalDateTime;

/**
 * DTO para representar um agendamento de mensagem.
 */
public record AppointmentDTO(
        Long id,
        LocalDateTime scheduleDate,
        String message,
        boolean sent,
        Long contactId,
        String contactName
) {
    public AppointmentDTO(Appointment entity) {
        this(
                entity.getId(),
                entity.getScheduleDate(),
                entity.getMessage(),
                entity.isSent(),
                entity.getContact().getId(),
                entity.getContact().getName()
        );
    }
}