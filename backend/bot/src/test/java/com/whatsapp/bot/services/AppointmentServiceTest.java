package com.whatsapp.bot.services;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.time.LocalDateTime;
import java.util.Optional;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import com.whatsapp.bot.dto.AppointmentDTO;
import com.whatsapp.bot.entities.Appointment;
import com.whatsapp.bot.entities.Contact;
import com.whatsapp.bot.repositories.AppointmentRepository;

class AppointmentServiceTest {

    @Mock
    private AppointmentRepository appointmentRepository;

    @InjectMocks
    private AppointmentService appointmentService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    @DisplayName("Deve salvar um novo agendamento corretamente")
    void testSaveAppointment() {
        Appointment appointment = new Appointment();
        Contact ctt = new Contact(1L, "joão silva");
        appointment.setId(1L);
        appointment.setContact(ctt);
        appointment.setScheduleDate(LocalDateTime.of(2025, 11, 10, 14, 30));

        when(appointmentRepository.save(any(Appointment.class))).thenReturn(appointment);

        AppointmentDTO saved = appointmentService.save(appointment);

        assertNotNull(saved);
        assertEquals(1L, saved.id());
        assertEquals(ctt.getName(), saved.contactName());
    }

    @Test
    @DisplayName("Deve buscar um agendamento existente por ID")
    void testFindById() {
        Contact ctt = new Contact(1L, "Maria Souza");
        Appointment appointment = new Appointment();
        appointment.setId(1L);

        appointment.setContact(ctt);

        when(appointmentRepository.findById(1L)).thenReturn(Optional.of(appointment));

        AppointmentDTO found = appointmentService.findOne(1L);

        assertTrue(found != null);
        assertEquals("Maria Souza", found.contactName());
        verify(appointmentRepository, times(1)).findById(1L);
    }

    @Test
    @DisplayName("Deve deletar um agendamento existente")
    void testDeleteAppointment() {
        Appointment appointment = new Appointment();
        Contact ctt = new Contact(1L, "joão silva");
        appointment.setId(1L);
        appointment.setContact(ctt);
        appointment.setScheduleDate(LocalDateTime.of(2025, 11, 10, 14, 30));

        // simula salvar
        when(appointmentRepository.save(any(Appointment.class))).thenReturn(appointment);
        appointmentService.save(appointment);

        // simula encontrar o registro
        when(appointmentRepository.findById(1L)).thenReturn(Optional.of(appointment));

        // simula exclusão
        doNothing().when(appointmentRepository).deleteById(1L);

        appointmentService.remove(appointmentService.findOne(1L));

        verify(appointmentRepository, times(1)).deleteById(1L);
    }

}
