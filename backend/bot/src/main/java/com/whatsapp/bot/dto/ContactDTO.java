package com.whatsapp.bot.dto;

import com.whatsapp.bot.entities.Contact;

public record ContactDTO(Long id, String name) {
	public ContactDTO(Contact contact) {
		this(contact.getId(), contact.getName());
	}
}
