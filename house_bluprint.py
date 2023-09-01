class House:
    def __init__(self, color, number_of_rooms, size):
        self.color = color
        self.number_of_rooms = number_of_rooms
        self.size = size  # in square feet
    
    def paint(self, new_color):
        self.color = new_color
        print(f"The house is now {self.color}")

    def add_room(self):
        self.number_of_rooms += 1
        print(f"The house now has {self.number_of_rooms} rooms")

    def remodel(self, new_size):
        self.size = new_size
        print(f"The house is now {self.size} square feet")


my_house = House("blue", 3, 1500)
your_house = House("red", 5, 2000)
