from .base_client import BaseClient

class ContactClient(BaseClient):
    """Cliente para os endpoints de ContactController"""

    def create_contact(self, contact: dict):
        """POST /contacts"""
        return self.post("/contacts", json=contact)

    def get_all_contacts(self):
        """GET /contacts"""
        return self.get("/contacts")

    def get_contact_by_id(self, contact_id: int):
        """GET /contacts/{id}"""
        return self.get(f"/contacts/{contact_id}")

    def update_contact(self, contact: dict):
        """PUT /contacts"""
        return self.put("/contacts", json=contact)

    def delete_contact(self, contact_id: int):
        """DELETE /contacts/{id}"""
        return self.delete(f"/contacts/{contact_id}")
