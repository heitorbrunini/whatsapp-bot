from .base_client import BaseClient

class AppointmentClient(BaseClient):
    """Cliente para os endpoints de AppointmentController"""

    def create_appointment(self, appointment: dict):
        """POST /appointments"""
        return self.post("/appointments", json=appointment)

    def get_all_appointments(self):
        """GET /appointments"""
        return self.get("/appointments")

    def get_appointment_by_id(self, appointment_id: int):
        """GET /appointments/{id}"""
        return self.get(f"/appointments/{appointment_id}")

    def update_appointment(self, appointment: dict):
        """PUT /appointments"""
        return self.put("/appointments", json=appointment)

    def delete_appointment(self, appointment_id: int):
        """DELETE /appointments/{id}"""
        return self.delete(f"/appointments/{appointment_id}")
