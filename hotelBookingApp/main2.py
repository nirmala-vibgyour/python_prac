import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "Real State Company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotel.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    """ class methods """
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    """ special/magic methods """
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

    # def __add__(self, other):
    #     total = self.price + other.price
    #     return total


class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.hotel_object = hotel_object
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    def generate(self):
        return "Hello, this is your digital ticket"

    def download(self):
        pass


hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

""" instance variable """
print(hotel1.name)
print(hotel2.name)

""" class variable: value is shared among each class instance """
print(hotel1.watermark)
print(hotel2.watermark)
print(Hotel.watermark)

""" instance methods and class methods ( together aka class attributes)
1. applied to the class instances (objects of the class)
2. print(Hotel.get_hotel_count(data=df)
3. print(hotel1.get_hotel_count(data=df)
"""
ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1)
print(ticket.the_customer_name)

convert = ReservationTicket.convert(10)
