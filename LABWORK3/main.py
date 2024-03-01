class HotelReservationSystem:
    def __init__(self):
        self.room_prices = {'single room': 100, 'double room': 150, 'suite': 250}
        self.additional_services = {'breakfast (per person)': 20, 'wifi (per day)': 10, 'parking (per day)': 15}

    def display_room_types(self):
        print("Available Room Types:")
        for i, (room_type, price) in enumerate(self.room_prices.items(), 1):
            print(f"{i}. {room_type} RM{price} per night")

    def select_room_type(self):
        self.display_room_types()
        while True:
            choice = input("Please select a room type either 1 or 2 or 3: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.room_prices):
                return list(self.room_prices.keys())[int(choice) - 1]

    def get_number_of_rooms(self):
        while True:
            num_rooms = input("Enter the number of rooms: ")
            if num_rooms.isdigit() and int(num_rooms) > 0:
                return int(num_rooms)

    def get_check_in_out_dates(self):
        check_in_date = input("Enter your check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter your check-out date (YYYY-MM-DD): ")
        return check_in_date, check_out_date

    def display_additional_services(self):
        print("\nAdditional Services:")
        for i, (service, price) in enumerate(self.additional_services.items(), 1):
            print(f"{i}. {service} - RM{price} ")

    def select_additional_services(self):
        self.display_additional_services()
        while True:
            choice = input("Would you like to add any additional services? (y/n): ")
            if choice.lower() == 'y':
                services = input("Please select additional services (separated by commas, example: 1,2): ")
                services = [int(service.strip()) for service in services.split(',')]
                return [list(self.additional_services.keys())[service - 1] for service in services]
            elif choice.lower() == 'n':
                return []

    def confirm_reservation(self, room_type, num_rooms, check_in_date, check_out_date, additional_services):
        print("\nThank you for your reservation.")
        print("Reservation Details:")
        print(f"Room Type: {room_type} Number of Rooms: {num_rooms}")
        print(f"Check-in Date: {check_in_date}")
        print(f"Check-out Date: {check_out_date}")

        if additional_services:
            print("\nAdditional Services:")
            for service in additional_services:
                print(f"- {service}")

        total_cost = self.calculate_total_cost(room_type, num_rooms, check_in_date, check_out_date, additional_services)
        print(f"\nTotal Cost: RM{total_cost}")

        confirmation = input("Would you like to confirm your reservation? (y/n): ")
        if confirmation.lower() == 'y':
            print("Reservation confirmed. Thank you for choosing our hotel. Enjoy your stay!")
        else:
            print("Reservation canceled. Thank you!")

    def calculate_total_cost(self, room_type, num_rooms, check_in_date, check_out_date, additional_services):
        room_price = self.room_prices[room_type]
        num_days = (int(check_out_date.split('-')[2]) - int(check_in_date.split('-')[2])) + 1
        total_cost = room_price * num_rooms * num_days
        for service in additional_services:
            total_cost += self.additional_services[service] * num_days
        return total_cost


def main():
    print("Welcome to Our Hotel Reservation System")
    hotel_system = HotelReservationSystem()
    room_type = hotel_system.select_room_type()
    num_rooms = hotel_system.get_number_of_rooms()
    check_in_date, check_out_date = hotel_system.get_check_in_out_dates()
    additional_services = hotel_system.select_additional_services()
    hotel_system.confirm_reservation(room_type, num_rooms, check_in_date, check_out_date, additional_services)


if __name__ == "__main__":
    main()
