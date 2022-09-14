class Vehicle:
    def __init__(self, obj):
        self.drive_obj = obj

    def drive(self):
        self.drive_obj.drive()
