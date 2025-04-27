class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0


    def available_seats(self):
        return self.total_seats - self.booked_seats
    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False
    def __str__(self):
        return f"Bus {self.number}"


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus
class Admin:
    def __init__(self):
       self.username = "admin"
       self.password = "1234"
    def login(self, username, password):
        return username == self.username and password == self.password
       
       
class BusSystem:
    fare = 500


    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin_logged_in = False
        self.admin = Admin()


    def add_bus(self, number, route, seats):
        if not self.admin_logged_in:
            print("access denied, Admin login required")
            return
        self.buses.append(Bus(number, route, seats))
        print(f"Bus: {number} added successfully")
    def show_buses(self):
        if not self.buses:
            print("no buses")
            return
        for bus in self.buses:
            print(f" bus number:{bus.number} | route: {bus.route}|total seats: {bus.total_seats}| available seats : {bus.available_seats()}")
    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus.number == bus_number:
                if bus.book_seat():
                    passenger = Passenger(name, phone, bus)
                    self.passengers.append(passenger)
                    print(f"ticket booked successfully for {name}. Fare: ${self.fare}")
                else:
                    print("No seats available on this bus")
                return
        print("Bus not there")


    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if self.admin.login(username, password):
            self.admin_logged_in = True
            print("adming login success")
            self.admin_menu()
        else:
            print("Invalid password")


    def admin_menu(self):
        while self.admin_logged_in:
            print("\n admin interface.")
            print("1. Add Bus")        
            print("2. View all buses ")
            print("3. Logout")
            choice = input("enter your choice: ")
           
            if choice == "1":
                number = input("enter bus number: ")
                route = input("enter route: ")
                try:
                    seats = int(input("enter total seats: "))
                    self.add_bus(number, route, seats)
                except ValueError:
                    print("invalid seat number")
            elif choice == "2":
                self.show_buses()
            elif choice == "3":
                self.admin_logged_in = False
                print("logged out from admin")
            else:
                print("invalid choice")


    def main_menu(self):
        while True:
            print("\n User menu:")
            print("1. user login:")
            print("2. Book Ticket")
            print("3. View buses")
            print("4. Exit")
            choice = input("enter ur choice: ")


            if choice == "1":
                self.admin_login()
            elif choice == "2":
                bus_number = input("enter bus number to book: ")
                name = input("enter your name: ")
                phone = input("enter your phone number: ")
                self.book_ticket(bus_number, name, phone)
            elif choice == "3":
                self.show_buses()
            elif choice == "4":
                print ("exit")
                break
            else:
                print("invalid choice")


system = BusSystem()
system.main_menu()                



