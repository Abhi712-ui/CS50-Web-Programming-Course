class point():
    def __init__(self, x, y): 
        self.x = x
        self.y = y


p = point(2, 8)

print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)
        return True

    def openSeats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["harry", "dick", "tom", "john"]
for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"Added {person} to flight sucessfully")
    else:
        print("No available seats") 
    