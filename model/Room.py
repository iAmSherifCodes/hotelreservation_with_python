from model.RoomType import RoomType
from model.iRoom import iRoom


class Room:
    def __init__(self, room_number, room_price, room_type=RoomType.name):
        self.room_number = room_number
        self.room_price = room_price
        self.room_type = room_type

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, room_number):
        self.room_number = room_number

    def get_room_price(self):
        return self.room_price

    def set_room_price(self, room_price):
        self.room_price = room_price





