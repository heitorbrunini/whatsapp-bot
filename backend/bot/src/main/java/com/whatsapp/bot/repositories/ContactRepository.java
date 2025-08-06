package com.whatsapp.bot.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.whatsapp.bot.entities.Contact;

public interface ContactRepository extends JpaRepository<Contact, Long> {

}
