class Address:
    def __init__(self, postal_code, city, street,
                 house_number, apartment_number):
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house_number = house_number
        self.apartment_number = apartment_number

    def __str__(self):
        return (f"{self.postal_code}, {self.city}, {self.street}, "
                f"{self.house_number} - {self.apartment_number}")
