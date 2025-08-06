package com.whatsapp.bot.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.whatsapp.bot.entities.Appointment;

public interface AppointmentRepository extends JpaRepository<Appointment, Long>{

}
