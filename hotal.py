def show_rooms():
    print("\nWelcome to Hotel Paradise")
    print("1. Single Room - Rs. 1000")
    print("2. Double Room - Rs. 2000")
    print("3. Suite - Rs. 5000")
    print()

def book_room():
    show_rooms()
    name = input("Enter your name: ")
    try:
        nights = int(input("How many nights? "))
        room_type = int(input("Choose room (1, 2, 3): "))
    except:
        print("Invalid input!")
        return

    if room_type == 1:
        room = "Single Room"
        cost = 1000
    elif room_type == 2:
        room = "Double Room"
        cost = 2000
    elif room_type == 3:
        room = "Suite"
        cost = 5000
    else:
        print("Wrong room type!")
        return

    total = cost * nights
    print("\nBooking Details:")
    print("Name:", name)
    print("Room:", room)
    print("Nights:", nights)
    print("Total Cost: Rs.", total)
    print("Booking Done\n")

def cancel_booking():
    name = input("\nEnter name for canceling: ")
    print("Booking canceled for", name, "\n")

def main():
    while True:
        print("\nHotel System")
        print("1. Book Room")
        print("2. Cancel Room")
        print("3. Exit")
        try:
            choice = int(input("Enter choice: "))
        except:
            print("Enter a number")
            continue

        if choice == 1:
            book_room()
        elif choice == 2:
            cancel_booking()
        elif choice == 3:
            print("Thank you Bye")
            break
        else:
            print("Wrong choice\n")

main()
