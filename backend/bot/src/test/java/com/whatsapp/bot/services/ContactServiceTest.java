package com.whatsapp.bot.services;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import java.util.List;
import java.util.Optional;
import java.util.Arrays;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import com.whatsapp.bot.dto.ContactDTO;
import com.whatsapp.bot.entities.Contact;
import com.whatsapp.bot.repositories.ContactRepository;

class ContactServiceTest {

    @Mock
    private ContactRepository contactRepository;

    @InjectMocks
    private ContactService contactService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    @DisplayName("Deve salvar um contato corretamente")
    void testSaveContact() {
        Contact contact = new Contact(1L, "João Silva");

        when(contactRepository.save(any(Contact.class))).thenReturn(contact);

        ContactDTO dto = contactService.save(contact);

        assertNotNull(dto);
        assertEquals("João Silva", dto.name());
        verify(contactRepository, times(1)).save(contact);
    }

    @Test
    @DisplayName("Deve retornar todos os contatos cadastrados")
    void testFindAllContacts() {
        Contact c1 = new Contact(1L, "João");
        Contact c2 = new Contact(2L, "Maria");
        when(contactRepository.findAll()).thenReturn(Arrays.asList(c1, c2));

        List<ContactDTO> result = contactService.findAll();

        assertEquals(2, result.size());
        assertEquals("João", result.get(0).name());
        assertEquals("Maria", result.get(1).name());
        verify(contactRepository, times(1)).findAll();
    }

    @Test
    @DisplayName("Deve retornar um contato pelo ID")
    void testFindOneContact() {
        Contact contact = new Contact(1L, "João Silva");
        when(contactRepository.findById(1L)).thenReturn(Optional.of(contact));

        ContactDTO dto = contactService.findOne(1L);

        assertNotNull(dto);
        assertEquals("João Silva", dto.name());
        verify(contactRepository, times(1)).findById(1L);
    }

    @Test
    @DisplayName("Deve remover um contato existente")
    void testDeleteContact() {
        Contact contact = new Contact(1L, "João Silva");
        ContactDTO dto = new ContactDTO(contact);

        doNothing().when(contactRepository).deleteById(1L);

        contactService.remove(dto);

        verify(contactRepository, times(1)).deleteById(1L);
    }
}
