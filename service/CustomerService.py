from model.Customer import Customer


class CustomerService(Customer):
    def __init__(self):
        self.email = ""
        self.first_name = ""
        self.last_name = ""

    def add_customer(self):