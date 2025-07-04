


class Display:
    pass

    def __init__(self, id, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return "Display 1: Welcome to the car park"