"""Class hotel representa el ejercicio realizado durante
ciertos metodos que aplican a un sistema de un hotel como: Crearlo,eliminarlo y mostrar su informacion etc"""


class Hotel:
    """Class representa los metodos de un cliente que pueden ser ejecutados"""
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms  # Un diccionario para almacenar la información de las habitaciones

    def create_hotel(self, name, rooms):
        """Crear un nuevo hotel."""
        if not name or not rooms or not isinstance(rooms, dict):
            raise ValueError("Informacion de cliente: Nombre,email y numero de telefono son necesarios.")
        self.name = name
        self.rooms = rooms

    def delete_hotel(self):
        """Eliminar la información del hotel."""
        self.name = ""
        self.rooms = {}

    def display_information(self):
        """Mostrar la información del hotel."""
        information = f"Hotel: {self.name}\nRooms:\n"
        for room_number, status in self.rooms.items():
            information += f"Room {room_number}: {'Occupied' if status else 'Available'}\n"
        return information

    def modify_hotel_information(self, new_name):
        """Modificar la información del hotel."""
        if not new_name:
            raise ValueError("New name cannot be empty.")
        self.name = new_name

    def reserve_room(self, room_number):
        """Reservar una habitación."""
        if not isinstance(room_number, int) or room_number not in self.rooms:
            raise ValueError("Invalid room number.")
        if not self.rooms[room_number]:
            self.rooms[room_number] = True
        return f"Room {room_number} reserved successfully."

    def cancel_reservation(self, room_number):
        """Cancelar una reservación."""
        if not isinstance(room_number, int) or room_number not in self.rooms:
            raise ValueError("Invalid room number.")

        if self.rooms[room_number]:
            self.rooms[room_number] = False
            return f"Reservation for Room {room_number} canceled."
        return f"No reservation found for Room {room_number}."
