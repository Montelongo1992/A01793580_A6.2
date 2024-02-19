"""Se importan las librerias necesarias para la ejecucion
correcta de las pruebas"""
import unittest
from unittest.mock import patch
import io
from reservation import Reservation


class TestReservationMethods(unittest.TestCase):
    """Class representa los metodos de pruebas unitarias por metodo de la clase reservation"""
    def setUp(self):
        # Configuración inicial para las pruebas
        self.reservation_manager = Reservation()

    def test_create_reservation(self):
        """probando la creacion de reservacion."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.reservation_manager.create_reservation(guest_name="Cristian", room_number=101, check_in_date="2024-02-16", check_out_date="2024-02-20")
            self.assertEqual(len(self.reservation_manager.reservations), 1)
            self.assertEqual(mock_stdout.getvalue().strip(), "Reservation created successfully.")

    def test_create_reservation_invalid_parameters(self):
        """probando la prueba negativa de reservaciones."""
        with self.assertRaises(ValueError):
            self.reservation_manager.create_reservation(guest_name="", room_number="", check_in_date="", check_out_date="")

    def test_cancel_reservation(self):
        """Probando la Cancelacion una reservacion."""
        # Agrega una reserva para cancelar
        self.reservation_manager.create_reservation(guest_name="Jane Smith", room_number=102, check_in_date="2024-02-18", check_out_date="2024-02-22")
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            # Intenta cancelar la reserva
            self.reservation_manager.cancel_reservation(guest_name="Jane Smith", room_number=102)
            self.assertEqual(len(self.reservation_manager.reservations), 0)
            self.assertEqual(mock_stdout.getvalue().strip(), "Reservation canceled successfully.")

    def test_cancel_reservation_no_matching(self):
        """Probando una cancelacion negativa."""
        with self.assertRaises(ValueError):
            self.reservation_manager.cancel_reservation(guest_name="Nonexistent Guest", room_number=999)
