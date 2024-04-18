# Refactoring the code according to the new requirements
import random
import string

class SeatBookingSystem:
    def _init_(self):
        # Each seat will now hold a dictionary for booking details or "F" if it is free.
        self.seats = {(row, col): "F" for row in range(1, 11) for col in range(1, 7)}
        # We'll use a set to store unique booking references.
        self.booking_references = set()

    def generate_booking_reference(self):
        """Generate a unique booking reference of 8 alphanumeric characters."""
        # Implementation of this function ensures that booking references are unique.
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        while reference in self.booking_references:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.booking_references.add(reference)
        return reference

    def check_availability(self, row, column):
        """Check if the specified seat is available."""
        # We now check if the seat is equal to "F".
        return self.seats[(row, column)] == "F"

    def book_seat(self, row, column, passport_number, first_name, last_name):
        """Book a seat and store passenger details if the seat is available."""
        if self.check_availability(row, column):
            booking_ref = self.generate_booking_reference()
            self.seats[(row, column)] = {
                'booking_ref': booking_ref,
                'passport_number': passport_number,
                'first_name': first_name,
                'last_name': last_name
            }
            return booking_ref
        return False

    def free_seat(self, row, column):
        """Free a seat if it is currently booked."""
        if self.seats[(row, column)] != "F":
            # Remove the booking reference from the set as well.
            del self.booking_references[self.seats[(row, column)]['booking_ref']]
            self.seats[(row, column)] = "F"
            return True
        return False

    def show_booking_status(self):
        """Show the booking status of all the seats."""
        for (row, column), details in self.seats.items():
            if details == "F":
                print(f"Seat {row}-{column} is available.")
            else:
                print(f"Seat {row}-{column} is booked: {details['booking_ref']} - {details['first_name']} {details['last_name']}")



