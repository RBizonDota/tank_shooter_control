

class Field:
    def __init__(self):
        self.my_tank_id = None
        self.data = None

    def update_data(self, new_data):
        self.data = new_data

    def set_tank_id(self, new_id):
        self.my_tank_id = new_id