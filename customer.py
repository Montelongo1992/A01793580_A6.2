"""Class representa el ejercicio realizado durante
ciertos metodos que aplican a un cliente como: Crearlo,eliminarlo y mostrar su informacion etc"""


class Customer:
    """Class representa los metodos de un cliente que pueden ser ejecutados"""
    def __init__(self):
        self.customers = []

    def create_customer(self, customer_name, email, phone_number):
        """Crear un nuevo cliente."""
        if not customer_name or not email or not phone_number:
            raise ValueError("Informacion de cliente: Nombre,email y numero de telefono son necesarios.")

        customer = {
            'customer_name': customer_name,
            'email': email,
            'phone_number': phone_number
        }
        self.customers.append(customer)
        print("Customer created successfully.")

    def delete_customer(self, customer_name):
        """Eliminar un cliente."""
        if not customer_name:
            raise ValueError("Customer name cannot be empty.")
        for customer in self.customers:
            if customer['customer_name'] == customer_name:
                self.customers.remove(customer)
                print("Customer deleted successfully.")
                return
        print("No matching customer found.")

    def display_customer_information(self):
        """Mostrar la información de los clientes."""
        if not self.customers:
            print("No customers available.")
        else:
            print("Customer Information:")
            for customer in self.customers:
                print(f"Name: {customer['customer_name']}, Email: {customer['email']}, Phone: {customer['phone_number']}")

    def modify_customer_information(self, customer_name, new_email, new_phone_number):
        """Modificar la información de un cliente."""
        if not customer_name:
            raise ValueError("Customer name cannot be empty.")

        customer_found = False
        for customer in self.customers:
            if customer['customer_name'] == customer_name:
                customer['email'] = new_email
                customer['phone_number'] = new_phone_number
                print("Customer information modified successfully.")
                customer_found = True
                break

        if not customer_found:
            raise ValueError("No matching customer found.")
