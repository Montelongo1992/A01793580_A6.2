"""Se importan las librerias necesarias para la ejecucion
correcta de las pruebas"""
import unittest
import unittest.mock
from hotel import Hotel


class TestHotelMethods(unittest.TestCase):
    """Class representa los metodos de pruebas unitarias por metodo de la clase hotel"""
    def setUp(self):
        self.hotel = Hotel(name="Sample Hotel", rooms={101: False, 102: True, 103: False})

    def test_create_hotel(self):
        """probando el metodo para la creacion de hotel."""
        self.hotel.create_hotel(name="New Hotel", rooms={201: False, 202: False})
        self.assertEqual(self.hotel.name, "New Hotel")
        self.assertEqual(self.hotel.rooms, {201: False, 202: False})

    def test_create_hotel_invalid_parameters(self):
        """probando el metodo para la creacion de hotel con datos invalidos de manera negativa."""
        with self.assertRaises(ValueError):
            self.hotel.create_hotel(name="", rooms={})
        with self.assertRaises(ValueError):
            self.hotel.create_hotel(name="Hotel", rooms="invalid_rooms")

    def test_delete_hotel(self):
        """probando el metodo para la eliminacion de hotel."""
        self.hotel.delete_hotel()
        self.assertEqual(self.hotel.name, "")
        self.assertEqual(self.hotel.rooms, {})

    def test_display_information(self):
        """probando el metodo para mostrar la informacion de hotel."""
        expected_output = "Hotel: Sample Hotel\nRooms:\nRoom 101: Available\nRoom 102: Occupied\nRoom 103: Available\n"
        self.assertEqual(self.hotel.display_information(), expected_output)

    def test_modify_hotel_information(self):
        """probando el metodo para modificar la informacion del hotel."""
        self.hotel.modify_hotel_information(new_name="Modified Hotel")
        self.assertEqual(self.hotel.name, "Modified Hotel")

    def test_modify_information_empty_name(self):
        """probando el metodo para la modificacion de informacion sin informacion de manera negativa."""
        with self.assertRaises(ValueError):
            self.hotel.modify_hotel_information(new_name="")

    def test_reserve_room(self):
        """probando el metodo para la creacion de de un cuarto."""
        result = self.hotel.reserve_room(room_number=101)
        self.assertEqual(result, "Room 101 reserved successfully.")
        self.assertTrue(self.hotel.rooms[101])

    def test_reserve_room_invalid_number(self):
        """probando el metodo para la creacion de un cuarto pero sin informacion o informacion invalida."""
        with self.assertRaises(ValueError):
            self.hotel.reserve_room(room_number=999)

    def test_cancel_reservation(self):
        """probando el metodo para la cancelacion de una reservacion."""
        result = self.hotel.cancel_reservation(room_number=102)
        self.assertEqual(result, "Reservation for Room 102 canceled.")
        self.assertFalse(self.hotel.rooms[102])

    def test_cancel_reservation_invalid_number(self):
        """probando el metodo para la cancelacion de una reservacion con informacion invalida."""
        with self.assertRaises(ValueError):
            self.hotel.cancel_reservation(room_number=999)

    def test_cancel_reservation_not_reserved(self):
        """probando el metodo para la cancelacion de una reservacion sin reserva."""
        result = self.hotel.cancel_reservation(room_number=101)
        self.assertEqual(result, "No reservation found for Room 101.")


if __name__ == '__main__':
    unittest.main()
