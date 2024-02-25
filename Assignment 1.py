from datetime import date
#Class one
class Customer:
    def __init__(self, name, lastName, age, phoneNumber, email, passportNumber, visa, passportExpDate, nationality):
        self._name = name
        self._lastName = lastName
        self._age = age
        self._phoneNumber = phoneNumber
        self._email = email
        self._passportNumber = passportNumber
        self._visa = visa
        self._passportExpDate = passportExpDate
        self._nationality = nationality

    # Getter and setter methods for each attribute
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_lastName(self):
        return self._lastName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_phoneNumber(self):
        return self._phoneNumber

    def set_phoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_passportNumber(self):
        return self._passportNumber

    def set_passportNumber(self, passportNumber):
        self._passportNumber = passportNumber

    def get_visa(self):
        return self._visa

    def set_visa(self, visa):
        self._visa = visa

    def get_passportExpDate(self):
        return self._passportExpDate

    def set_passportExpDate(self, passportExpDate):
        self._passportExpDate = passportExpDate

    def get_nationality(self):
        return self._nationality

    def set_nationality(self, nationality):
        self._nationality = nationality

    # Placeholder function headers
    def view_booking_history(self):
        """
        View the booking history of the customer.
        """
        pass


#class two
from datetime import date

class AirlineEmployee:
    def __init__(self, name, lastName, age, phoneNumber, email, workID):
        self._name = name
        self._lastName = lastName
        self._age = age
        self._phoneNumber = phoneNumber
        self._email = email
        self._workID = workID

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_lastName(self):
        return self._lastName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_phoneNumber(self):
        return self._phoneNumber

    def set_phoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_workID(self):
        return self._workID

    def set_workID(self, workID):
        self._workID = workID

    # Placeholder function headers
    def view_schedule(self):
        """
        View the schedule of the airline employee.
        """
        pass
#Class Three

class BoardingPass:
    def __init__(self, passenger_name, from_location, to_location, flight_number, date, time, gate, boarding_time, seat_number, arrival_time, terminal, electronic_ticket_number):
        self._passenger_name = passenger_name
        self._from_location = from_location
        self._to_location = to_location
        self._flight_number = flight_number
        self._date = date
        self._time = time
        self._gate = gate
        self._boarding_time = boarding_time
        self._seat_number = seat_number
        self._arrival_time = arrival_time
        self._terminal = terminal
        self._electronic_ticket_number = electronic_ticket_number

    # Getter methods for each attribute
    def get_passenger_name(self):
        return self._passenger_name

    def get_from_location(self):
        return self._from_location

    def get_to_location(self):
        return self._to_location

    def get_flight_number(self):
        return self._flight_number

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_gate(self):
        return self._gate

    def get_boarding_time(self):
        return self._boarding_time

    def get_seat_number(self):
        return self._seat_number

    def get_arrival_time(self):
        return self._arrival_time

    def get_terminal(self):
        return self._terminal

    def get_electronic_ticket_number(self):
        return self._electronic_ticket_number

    # Setter methods for each attribute
    def set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    def set_from_location(self, from_location):
        self._from_location = from_location

    def set_to_location(self, to_location):
        self._to_location = to_location

    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def set_date(self, date):
        self._date = date

    def set_time(self, time):
        self._time = time

    def set_gate(self, gate):
        self._gate = gate

    def set_boarding_time(self, boarding_time):
        self._boarding_time = boarding_time

    def set_seat_number(self, seat_number):
        self._seat_number = seat_number

    def set_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time

    def set_terminal(self, terminal):
        self._terminal = terminal

    def set_electronic_ticket_number(self, electronic_ticket_number):
        self._electronic_ticket_number = electronic_ticket_number

    # Placeholder function headers
    def update_gate(self, new_gate):
        """
        Update the boarding gate information for the flight.
        """
        pass

# class four
from enum import Enum

class Classes(Enum):
    ECONOMY_CLASS = "Economy class"
    BUSINESS_CLASS = "Business class"
    FIRST_CLASS = "First class"

class Airplane:
    def __init__(self, model, color, engine, wings, tail, num_seats, classes, year_of_production):
        self._model = model
        self._color = color
        self._engine = engine
        self._wings = wings
        self._tail = tail
        self._num_seats = num_seats
        self._classes = classes
        self._year_of_production = year_of_production

    # Getter and setter methods for each attribute
    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_engine(self):
        return self._engine

    def set_engine(self, engine):
        self._engine = engine

    def get_wings(self):
        return self._wings

    def set_wings(self, wings):
        self._wings = wings

    def get_tail(self):
        return self._tail

    def set_tail(self, tail):
        self._tail = tail

    def get_num_seats(self):
        return self._num_seats

    def set_num_seats(self, num_seats):
        self._num_seats = num_seats

    def get_classes(self):
        return self._classes

    def get_year_of_production(self):
        return self._year_of_production

    def set_year_of_production(self, year_of_production):
        self._year_of_production = year_of_production

    # Placeholder function headers

    def check_engine(self):
        """
        Check the status of the airplane's engine.
        """
        pass


# Example usage Class one:
customer1 = Customer("Khaled", "ALharmoodi", 19, "12345", "khaled.alharmoodi@example.com", "AB999", "Tourist", "2028-12-1", "UAE")


print("Customer Name:", customer1.get_name())
print("Customer Last Name:", customer1.get_lastName())
print("Customer Age:", customer1.get_age())
print("Customer Phone Number:", customer1.get_phoneNumber())
print("Customer Email:", customer1.get_email())
print("Customer Passport Number:", customer1.get_passportNumber())
print("Customer Visa:", customer1.get_visa())
print("Customer Passport Expiry Date:", customer1.get_passportExpDate())
print("Customer Nationality:", customer1.get_nationality())

# Example usage class two :
employee1 = AirlineEmployee("Sara", "Targaryen", 27, "1232390", "sara.targaryen@example.com", "EMP223")
print("Employee Name:", employee1.get_name())  # Output: Sara
print("Employee Last Name:", employee1.get_lastName())  # Output: Targaryen
print("Employee Age:", employee1.get_age())  # Output: 27
print("Employee Phone Number:", employee1.get_phoneNumber())  # Output: 1232390
print("Employee Email:", employee1.get_email())  # Output: sara.targaryen@example.com
print("Employee Work ID:", employee1.get_workID())  # Output: EMP223

# Example usage class three:
boarding_pass1 = BoardingPass("Professor: Sujith Mathew", "New York", "Abu Dhabi", "AB123", "2024-03-21", "10:00", "A1", "09:30", "11A", "12:30", "Terminal 3", "1234522890")

print("Passenger Name:", boarding_pass1.get_passenger_name()) # Output: Professor: Sujith Mathew
print("From:", boarding_pass1.get_from_location()) # Output: New York
print("To:", boarding_pass1.get_to_location()) # Output: Abu Dhabi
print("Flight Number:", boarding_pass1.get_flight_number()) # Output: AB123
print("Date:", boarding_pass1.get_date()) # Output: 2024-03-21
print("Time:", boarding_pass1.get_time()) # Output: 10:00
print("Gate:", boarding_pass1.get_gate()) # Output: A1
print("Boarding Time:", boarding_pass1.get_boarding_time()) # Output: 09:30
print("Seat Number:", boarding_pass1.get_seat_number()) # Output: 11A
print("Arrival Time:", boarding_pass1.get_arrival_time()) # Output: 12:30
print("Terminal:", boarding_pass1.get_terminal())# Output: Terminal 3
print("Electronic Ticket Number:", boarding_pass1.get_electronic_ticket_number())# Output:1234522890

# Example usage class four:
plane = Airplane("Boeing 737", "White", "Jet", "Fixed-wing", "Conventional", 150, Classes.ECONOMY_CLASS, 2020)
print("Model:", plane.get_model()) # Output:Boeing 737
print("Color:", plane.get_color()) # Output:White
print("Engine:", plane.get_engine()) # Output:Jet
print("Wings:", plane.get_wings()) # Output:Fixed-wing
print("Tail:", plane.get_tail())  # Output:Conventional
print("Number of Seats:", plane.get_num_seats()) #Output: 150
print("Classes:", plane.get_classes()) #Output: ECONOMY_CLASS
print("Year of Production:", plane.get_year_of_production()) #Output: 2020