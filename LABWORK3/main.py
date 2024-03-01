"""
 Program purpose: To create FairView Hotel Reservation System
 Programmer: NOORALIA EVIEANNA SOFEA BINTI NORHAIZAM
 Date: 1 March 2024
"""
from datetime import datetime

# Define nightly rates
room_types = ["single", "double", "suite"]
rates = [100, 150, 250]

add_services = {"breakfast (per person)": 20, "wifi (per day)": 10, "parking (per day)": 15}

def calculateCost(room_type, no_room, check_in_date, check_out_date, add_services):
    if room_type in range(1, 4):
        num_nights = (check_out_date - check_in_date).days
        base_cost = rates[room_type - 1] * no_room * num_nights
        additional_cost = sum(add_services.values())
        total_cost = base_cost + additional_cost
        return total_cost
    else:
        return None

def main():
    print("Welcome to the Fairview Hotel Reservation System")
    # Availability of room type
    print("Available Room Types:")
    for i, room_type in enumerate(room_types):
        print(f"{i+1}. {room_type} - RM{rates[i]} per night")

    room_type = int(input("Please select a room type either 1 or 2 or 3: "))
    no_room = int(input("Enter the number of rooms: "))
    check_in_date = datetime.strptime(input("Enter check-in date (YYYY-MM-DD): "), '%Y-%m-%d')
    check_out_date = datetime.strptime(input("Enter check-out date (YYYY-MM-DD): "), '%Y-%m-%d')

    print("Additional Services:")
    for i, (service, price) in enumerate(add_services.items(), start=1):
        print(f"{i}. {service} - RM{price} ")

    selected_services = {}
    for service in add_services:
        choice = input(f"Add {service} for RM{add_services[service]}  (y/n): ").lower()
        if choice == "y":
            selected_services[service] = add_services[service]

    total_cost = calculateCost(room_type, no_room, check_in_date, check_out_date, selected_services)

    if total_cost is not None:
        print("\nThank you for your reservation.")
        print("\nReservation Details:")
        print(f"Room Type: {room_types[room_type - 1]}")
        print(f"Number of Rooms: {no_room}")
        print(f"Check-in Date: {check_in_date.strftime('%Y-%m-%d')}")
        print(f"Check-out Date: {check_out_date.strftime('%Y-%m-%d')}")
        print("Additional Services:")
        for service in selected_services:
            print(f"- {service}")
        print(f"Total Cost for Reservation: RM{total_cost:.2f}")
        # Customer need to confirm their reservation
        confirm_booking = input("\nWould you like to confirm your reservation?(y/n):").lower()
        if confirm_booking == "y":
            print("\nYour reservation is confirmed. Thank you for choosing FairView Hotel and enjoy your stay!")
        else:
            print("Reservation not confirmed. Thank you for considering us.")
    else:
        print("Invalid room type. Please select a valid room type.")

if __name__ == "__main__":
    main()
