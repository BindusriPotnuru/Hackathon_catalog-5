from datetime import datetime

# Sample data: List of charging stations
charging_stations = [
    {"id": 1, "name": "Station A", "location": "Location X", "available_slots": 5},
    {"id": 2, "name": "Station B", "location": "Location Y", "available_slots": 3},
    {"id": 3, "name": "Station C", "location": "Location Z", "available_slots": 2},
]

# Sample data: List of bookings
bookings = []

# Function to display all charging stations
def display_stations(stations):
    print("\nAvailable Charging Stations:")
    for station in stations:
        print(f"ID: {station['id']}, Name: {station['name']}, Location: {station['location']}, Available Slots: {station['available_slots']}")

# Function to filter stations by location
def filter_stations(location):
    return [station for station in charging_stations if station["location"].lower() == location.lower()]

# Function to book a slot at a station
def book_slot(station_id, user_name, booking_time):
    for station in charging_stations:
        if station["id"] == station_id:
            if station["available_slots"] > 0:
                station["available_slots"] -= 1
                bookings.append({
                    "station_id": station_id,
                    "user_name": user_name,
                    "booking_time": booking_time
                })
                print(f"\nSlot booked successfully for {user_name} at {station['name']} on {booking_time}.")
                return
            else:
                print("\nNo available slots at this station.")
                return
    print("\nInvalid station ID.")

# Main program loop
def main():
    while True:
        print("\n1. View All Charging Stations")
        print("2. Filter Stations by Location")
        print("3. Book a Slot")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_stations(charging_stations)

        elif choice == "2":
            location = input("Enter location to filter: ")
            filtered_stations = filter_stations(location)
            if filtered_stations:
                display_stations(filtered_stations)
            else:
                print(f"\nNo stations found in location '{location}'.")

        elif choice == "3":
            station_id = int(input("Enter the station ID to book: "))
            user_name = input("Enter your name: ")
            booking_time = input("Enter booking time (YYYY-MM-DD HH:MM:SS): ")
            booking_time = datetime.strptime(booking_time, "%Y-%m-%d %H:%M:%S")
            book_slot(station_id, user_name, booking_time)

        elif choice == "4":
            print("\nExiting the program.")
            break

        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()
