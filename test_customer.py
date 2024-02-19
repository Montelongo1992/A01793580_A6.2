"""Se importan las librerias necesarias para la ejecucion
correcta de las pruebas"""
import unittest
from unittest.mock import patch
import io
from customer import Customer  # Asegúrate de importar la clase Customer


class TestCustomerMethods(unittest.TestCase):
    """Class representa los metodos de pruebas unitarias por metodo de la clase Customer"""
    def setUp(self):
        # Configuración inicial para las pruebas
        self.customer_manager = Customer()

    def test_create_customer(self):
        """probando el metodo para la creacion de customer."""
        self.customer_manager.create_customer(customer_name="Cristian", email="cristian@example.com", phone_number="123-456-7890")
        self.assertEqual(len(self.customer_manager.customers), 1)

    def test_create_customer_invalid_information(self):
        """probando el metodo para la creacion de reservacion de manera negativa."""
        with self.assertRaises(ValueError):
            self.customer_manager.create_customer(customer_name="", email="", phone_number="")

    def test_create_customer_missing_name(self):
        """probando el metodo para la creacion de cliente de manera negativa."""
        with self.assertRaises(ValueError):
            self.customer_manager.create_customer(customer_name="", email="cristian@example.com", phone_number="123-456-7890")

    def test_create_customer_missing_email(self):
        """probando el metodo para la creacion de email de manera negativa."""
        with self.assertRaises(ValueError):
            self.customer_manager.create_customer(customer_name="cristian", email="", phone_number="123-456-7890")

    def test_create_customer_missing_phone_number(self):
        """probando el metodo para la creacion de numero de telefono de manera negativa."""
        with self.assertRaises(ValueError):
            self.customer_manager.create_customer(customer_name="cristian", email="cristian@example.com", phone_number="")

    def test_delete_customer(self):
        """probando el metodo para eliminar cliente."""
        # Agrega un cliente para eliminar
        self.customer_manager.create_customer(customer_name="Jhovany Montelongo", email="jho@example.com", phone_number="987-654-3210")
        # Intenta eliminar el cliente
        self.customer_manager.delete_customer(customer_name="Jhovany Montelongo")
        self.assertEqual(len(self.customer_manager.customers), 0)

    def test_delete_customer_invalid_name(self):
        """probando el metodo para eliminar cliente de forma negativa con informacion invalida"""
        with self.assertRaises(ValueError):
            self.customer_manager.delete_customer(customer_name="")

    def test_display_customer_information(self):
        """probando el metodo para mostrar la informacion de un cliente."""
        # Agrega algunos clientes
        self.customer_manager.create_customer(customer_name="cristian", email="cristian@example.com", phone_number="123-456-7890")
        self.customer_manager.create_customer(customer_name="jhovany", email="jhovany@example.com", phone_number="987-654-3210")
        # Verifica que la información se muestre correctamente
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.customer_manager.display_customer_information()
            expected_output = "Customer Information:\nName: cristian, Email: cristian@example.com, Phone: 123-456-7890\nName: jhovany, Email: jhovany@example.com, Phone: 987-654-3210\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_modify_customer_information(self):
        """probando el metodo para modificar la informacion de un cliente."""
        # Agrega un cliente para modificar
        self.customer_manager.create_customer(customer_name="cristian", email="cristian@example.com", phone_number="123-456-7890")
        # Modifica la información del cliente
        self.customer_manager.modify_customer_information(customer_name="cristian", new_email="cristian.mon@example.com", new_phone_number="987-654-3210")
        modified_customer = self.customer_manager.customers[0]
        self.assertEqual(modified_customer['email'], "cristian.mon@example.com")
        self.assertEqual(modified_customer['phone_number'], "987-654-3210")

    def test_modify_customer_information_no_matching(self):
        """probando el metodo para mostrar la informacion de un cliente con informacion que existe."""
        with self.assertRaises(ValueError):
            self.customer_manager.modify_customer_information(customer_name="Nonexistent Customer", new_email="new@example.com", new_phone_number="555-555-5555")

    def test_modify_customer_information_empty_name(self):
        """probando el metodo para modificar la informacion de un cliente con informacion vacia."""
        with self.assertRaises(ValueError):
            self.customer_manager.modify_customer_information(customer_name="", new_email="new@example.com", new_phone_number="555-555-5555")


if __name__ == '__main__':
    unittest.main()
