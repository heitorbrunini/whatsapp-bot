package com.whatsapp.bot.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.whatsapp.bot.dto.ContactDTO;
import com.whatsapp.bot.entities.Contact;
import com.whatsapp.bot.services.ContactService;

@RestController
@RequestMapping("/contacts")
@CrossOrigin(origins = "*")
public class ContactController {

    @Autowired
    private ContactService service;

    @PostMapping
    public ContactDTO createContact(@RequestBody Contact contact) {
        return service.save(contact);
    }

    @GetMapping
    public List<ContactDTO> getAllContacts() {
        return service.findAll();
    }

    @GetMapping("/{id}")
    public ContactDTO getContactById(@PathVariable Long id) {
        return service.findOne(id);
    }

    @PutMapping
    public ContactDTO updateContact(@RequestBody Contact contact) {

          return service.update(contact);
    }

    @DeleteMapping("/{id}")
    public void deleteContact(@PathVariable Long id) {
        ContactDTO contact = service.findOne(id);
        service.remove(contact);
    }
}
