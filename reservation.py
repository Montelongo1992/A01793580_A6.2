"""Class representa el ejercicio realizado durante una reservacion"""


class Reservation:
    """Class representa clase reservation de un hotel"""
    def __init__(self):
        self.reservations = []

    def create_reservation(self, guest_name, room_number, check_in_date, check_out_date):
        """Metodo crear una nueva reserva."""
        if not guest_name or not isinstance(room_number, int) or not isinstance(check_in_date, str) or not isinstance(check_out_date, str):
            raise ValueError("Invalid parameters for reservation.")
        reservation = {
            'guest_name': guest_name,
            'room_number': room_number,
            'check_in_date': check_in_date,
            'check_out_date': check_out_date
        }
        self.reservations.append(reservation)
        print("Reservation created successfully.")

    def cancel_reservation(self, guest_name, room_number):
        """Metodos cancelar una reserva."""
        if not guest_name or not isinstance(room_number, int):
            raise ValueError("parametros invalidos para cancelar reservation.")

        matching_reservations = [reservation for reservation in self.reservations if reservation['guest_name'] == guest_name and reservation['room_number'] == room_number]

        if not matching_reservations:
            raise ValueError("No matching reservation found.")
        for reservation in matching_reservations:
            self.reservations.remove(reservation)
            print("Reservation canceled successfully.")
