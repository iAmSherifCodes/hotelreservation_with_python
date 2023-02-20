from model.Room import Room


class FreeRoom(Room):
    def __init__(self, room_number, room_price):
        super().__init__(room_number, room_price)
        self.room_price = 0

    def __str__(self):
        return f"FreeRoom price is {self.room_price}"
