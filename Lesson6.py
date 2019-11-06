class time:
    """Blueprint for a time object"""
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
    
    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print(self.hour, ":", self.minute, ":", self.second)

# First time object
my_time1 = time()
my_time1.print_time()
my_time1.set_time(1, 2, 3)

# Second time object
my_time2 = time()
my_time2.set_time(12,0, 0)

print("My two time objects are now storing: ")
my_time1.print_time()
my_time2.print_time()
