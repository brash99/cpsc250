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
        # self.first_name is a string
        # '' is an empty string
        # comparison = True if self.first_name is an empty string
        # otherwise, comparison = False
        comparison = self.first_name == ''
        return comparison

    def print_seat(self):
        print(f'{self.first_name} {self.last_name}, Paid: ${self.paid:.2f}')


# Create and print a list of the current seat status (T = Empty, F = Reserved)
def print_seats(plane):
    global num_seats
    seat_status_is_empty = []
    for ii in range(num_seats):
        seat_status_is_empty.append(plane[ii].is_empty())
    print("Current Seat Status (T = Empty, F = Reserved):")
    print(seat_status_is_empty)


# Print the passenger list - only print seats that are NOT empty
def print_passenger_list(plane):
    global num_seats
    for ii in range(num_seats):
        if not plane[ii].is_empty():
            print(f'{ii}:', end=' ')
            plane[ii].print_seat()


# Reserve a seat.  Make sure that seat is empty!
def reserve_seat(plane):
    seat_num = int(input('Enter seat num:\n'))
    if not plane[seat_num].is_empty():
        print('Seat not empty')
    else:
        firstname = input('Enter first name:\n')
        lastname = input('Enter last name:\n')
        paid = float(input('Enter amount paid:\n'))
        plane[seat_num].reserve(firstname, lastname, paid)

def cancel_flight(plane):
    # Use the value of num_seats from the main program
    global num_seats

    check_for_sure = input('Are you sure you want to cancel the entire flight? (y/n)\n')
    if check_for_sure == 'y':
        for i in range(num_seats):
            plane[i].make_empty()

# Main program

if __name__ == '__main__':

    # Initialize a list of Seat() objects
    #
    # Create a Python list called my_plane of 10 seats, all of which are empty
    #
    num_seats = 10
    my_plane = []
    for i in range(num_seats):
        my_plane.append(Seat())

    print_seats(my_plane)

    # Write a menu loop to take commands from the user
    #
    # p = print seat status for the entire plane
    # l = list all passengers with reservations (print only non-empty seats)
    # r = reserve a seat
    # c = cancel the entire flight
    # q = quit

    # get choice from user
    command = input('Enter command (p/l/r/c/q):\n')

    while command != 'q':
        if command == 'p':  # Print seats
            print_seats(my_plane)
        elif command == 'r':  # Reserve a seat
            reserve_seat(my_plane)
        elif command == 'l':  # List passengers
            print_passenger_list(my_plane)
        elif command == 'c':  # Cancel the entire flight
            cancel_flight(my_plane)
        else:
            print('Invalid command.')

        command = input('Enter command (p/l/r/c/q):\n')
