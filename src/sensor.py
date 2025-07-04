


class CarPark:
    pass
    def __init__(self, location, capacity, plates = None, displays = None):
        #parameters
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.displays = displays or []

    def __str__(self):
        ... # Return string containing the car park's location and capacity.