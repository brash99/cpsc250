class Seat:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0

    def reserve(self, f_name, l_name, amt_paid):
        self.first_name = f_name
        self.last_name = l_name
        self.paid = amt_paid

    def make_empty(self):
        self.__init__()

    def is_empty(self):
        return self.first_name == ''

    def print_seat(self):
        print(f'{self.first_name} {self.last_name}, Paid: {self.paid:.2f}')


# Create and print a list of the current seat status (T = Empty, F = Reserved)
def print_seats(seats):
    global num_seats
    seat_status_is_empty = []
    for ii in range(num_seats):
        seat_status_is_empty.append(seats[ii].is_empty())
    print("Current Seat Status (T = Empty, F = Reserved):")
    print(seat_status_is_empty)


# Print the passenger list - only print seats that are NOT empty
def print_passenger_list(seats):
    global num_seats
    for ii in range(num_seats):
        if not seats[ii].is_empty():
            print(f'{ii}:', end=' ')
            seats[ii].print_seat()


# Reserve a seat.  Make sure that seat is empty!
def reserve_seat(seats):
    seat_num = int(input('Enter seat num:\n'))
    if not seats[seat_num].is_empty():
        print('Seat not empty')
    else:
        firstname = input('Enter first name:\n')
        lastname = input('Enter last name:\n')
        paid = float(input('Enter amount paid:\n'))
        seats[seat_num].reserve(firstname, lastname, paid)


# Main program

# Initialize a list of Seat() objects
num_seats = 10
available_seats = []
for i in range(num_seats):
    available_seats.append(Seat())

# Write a menu loop to take commands from the user
#
# p = print seat status
# l = list all passengers with reservations
# r = reserve a seat
# q = quit

command = input('Enter command (p/l/r/q):\n')
while command != 'q':
    if command == 'p':  # Print seats
        print_seats(available_seats)
    elif command == 'r':  # Reserve a seat
        reserve_seat(available_seats)
    elif command == 'l':  # List passengers
        print_passenger_list(available_seats)
    else:
        print('Invalid command.')

    command = input('Enter command (p/l/r/q):\n')
