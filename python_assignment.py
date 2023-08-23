# YOUR Pyhton code.....
class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
        self.city_codes = {
            "BLR": "Bengaluru",
            "BOM": "Mumbai",
            "BBI": "Bhubaneswar",
            "HYD": "Hyderabad",
            "JLR": "Jabalpur"
        }

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        city_flights = [flight for flight in self.flights if flight.source == city or flight.destination == city]
        return city_flights

    def search_by_source(self, source):
        source_flights = [flight for flight in self.flights if flight.source == source]
        return source_flights

    def search_between_cities(self, source, destination):
        city_pairs_flights = [flight for flight in self.flights if flight.source == source and flight.destination == destination]
        return city_pairs_flights

    def print_flights(self, flight_list):
        if not flight_list:
            print("No flights found.")
            return
        
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in flight_list:
            print(f"{flight.flight_id}\t{self.city_codes[flight.source]}\t{self.city_codes[flight.destination]}\t{flight.price}")


def main():
    flight_table = FlightTable()
    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    print("Search Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        city = input("Enter the city code: ").upper()
        city_flights = flight_table.search_by_city(city)
        flight_table.print_flights(city_flights)
    elif choice == 2:
        source = input("Enter the source city code: ").upper()
        source_flights = flight_table.search_by_source(source)
        flight_table.print_flights(source_flights)
    elif choice == 3:
        source = input("Enter the source city code: ").upper()
        destination = input("Enter the destination city code: ").upper()
        city_pairs_flights = flight_table.search_between_cities(source, destination)
        flight_table.print_flights(city_pairs_flights)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
