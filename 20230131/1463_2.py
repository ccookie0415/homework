class PublicTransport:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
        self.passenger_count = 0

    def get_in(self, passenger_count):
        self.passenger_count += passenger_count

    def get_off(self, passenger_count):
        self.passenger_count -= passenger_count

    def current_passenger_count(self):
        return self.passenger_count
    
bus = PublicTransport("Bus", 2.5)
print("Before getting in: ", bus.current_passenger_count()) # 0

bus.get_in(10)
print("After getting in 10 passengers: ", bus.current_passenger_count()) # 10

bus.get_off(5)
print("After getting off 5 passengers: ", bus.current_passenger_count()) # 5

bus.get_off(10)
print("After getting off 10 passengers: ", bus.current_passenger_count()) # 0  