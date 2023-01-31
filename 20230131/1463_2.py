class PublicTransport:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
        self.passenger_count = 0
        self.all_passenger = 0

    def get_in(self, passenger_count):
        self.passenger_count += passenger_count
        self.all_passenger += passenger_count

    def get_off(self, passenger_count):
        self.passenger_count -= passenger_count

    def current_passenger_count(self):
        return self.passenger_count
    
    def profit(self):
        return self.fare * self.all_passenger
    
bus = PublicTransport("Bus", 2.5)
print(bus.current_passenger_count()) # 0

bus.get_in(30)
print(bus.current_passenger_count()) # 10

bus.get_off(5)
print(bus.current_passenger_count()) # 5

bus.get_off(10)
print(bus.current_passenger_count()) # 0  

print(bus.profit()) # 75 (30 passengers * fare 2.5)
