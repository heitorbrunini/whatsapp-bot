package com.whatsapp.bot.services;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.whatsapp.bot.dto.ContactDTO;
import com.whatsapp.bot.entities.Contact;
import com.whatsapp.bot.repositories.ContactRepository;

@Service
public class ContactService {
	
	@Autowired
	private ContactRepository repository;
	
	public List<ContactDTO> findAll(){
		
		List<ContactDTO> dtos = new ArrayList<>(); 
		
		List<Contact> data = repository.findAll();
		data.forEach(ctt -> dtos.add(new ContactDTO(ctt)));
		
		return dtos;
		
	}
	
	
}
