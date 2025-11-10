package com.whatsapp.bot.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.whatsapp.bot.dto.AppointmentDTO;
import com.whatsapp.bot.entities.Appointment;
import com.whatsapp.bot.services.AppointmentService;

@RestController
@RequestMapping("/appointments")
@CrossOrigin(origins = "*")
public class AppointmentController {

    @Autowired
    private AppointmentService service;

    @PostMapping
    public AppointmentDTO createAppointment(@RequestBody Appointment appointment) {
        return service.save(appointment);
    }

    @GetMapping
    public List<AppointmentDTO> getAllAppointments() {
        return service.findAll();
    }

    @GetMapping("/{id}")
    public AppointmentDTO getAppointmentById(@PathVariable Long id) {
        return service.findOne(id);
    }

    @PutMapping("/{id}")
    public AppointmentDTO updateAppointment( @RequestBody AppointmentDTO appointmentDTO ) {
        // Garante que o ID recebido via path é usado
    	
        return service.update(appointmentDTO);
    }

    @DeleteMapping("/{id}")
    public void deleteAppointment(@PathVariable Long id) {
        AppointmentDTO appointment = service.findOne(id);
        service.remove(appointment);
    }
}
