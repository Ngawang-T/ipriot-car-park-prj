


class CarPark:
    pass

    class CarPark:
        pass

        def __init__(self, location, capacity, plates=None, displays=None):
            # parameters
            self.location = location
            self.capacity = capacity
            self.plates = plates
            self.displays = displays or []

        def __str__(self):
            return "Car park at 777 random named Street, with 100 bays"