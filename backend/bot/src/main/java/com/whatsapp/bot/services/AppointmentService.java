package com.whatsapp.bot.services;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.whatsapp.bot.dto.AppointmentDTO;
import com.whatsapp.bot.entities.Appointment;
import com.whatsapp.bot.repositories.AppointmentRepository;


@Service
public class AppointmentService {
	
	@Autowired
	private AppointmentRepository repository;
	
	public AppointmentDTO save(Appointment data) {
		
		repository.saveAndFlush(data);
		
		return new AppointmentDTO(data);

	}
	
	public List<AppointmentDTO> findAll(){
		List<AppointmentDTO> dtos = new ArrayList<>();
		List<Appointment> data = repository.findAll();
		
		data.forEach(apt -> dtos.add(new AppointmentDTO(apt)));
		
		return dtos;
	}
	
	public void remove(AppointmentDTO dto) {
		repository.deleteById(dto.id());
	}
	
	public AppointmentDTO update(AppointmentDTO dto) {
		
		Appointment data = repository.findById(dto.id()).get();
		
		data.setMessage(dto.message());
		data.setScheduleDate(dto.scheduleDate());
		data.setSent(dto.sent());
		
		repository.saveAndFlush(data);
		
		return dto;		
	}
	
	public AppointmentDTO findOne(Long id) {
		return new AppointmentDTO(repository.findById(id).get());
	}
	
}
