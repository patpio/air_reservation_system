from pprint import pprint


class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

        self.rows, self.seats = self.airplane.seating_plan()
        self.seating_plan = [None] + [{seat: None for seat in self.seats} for _ in self.rows]

    def get_airlines(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.airplane.get_name()

    def _parse_seat(self, seat):
        letter = seat[-1]
        if letter not in self.seats:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row number {row_text}')

        if row not in self.rows:
            raise ValueError(f'Row number is out of range {row}')

        return row, letter

    def check_place(self, row, letter, seat):
        if self.seating_plan[row][letter] is not None:
            raise ValueError(f'Seat {seat} is already taken')

    def allocate_passenger(self, passenger='Pat P', seat='12C'):
        row, letter = self._parse_seat(seat)

        self.check_place(row, letter, seat)
        self.seating_plan[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):
        row_old, letter_old = self._parse_seat(seat_from)

        if self.seating_plan[row_old][letter_old] is None:
            raise ValueError(f'Seat {seat_from} is not taken')

        row_new, letter_new = self._parse_seat(seat_to)

        self.check_place(row_new, letter_new, seat_to)
        self.seating_plan[row_new][letter_new] = self.seating_plan[row_old][letter_old]
        self.seating_plan[row_old][letter_old] = None

    def num_empty_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None) for row in self.seating_plan if row is not None)

    def print_cards(self, printer):
        passengers = self.get_passengers()

        for passenger, seat in passengers:
            printer(passenger, seat, self.get_airplane_model(), self.flight_number)

    def get_passengers(self):
        passengers = []

        rows, letters = self.airplane.seating_plan()

        for row in rows:
            for letter in letters:
                passenger = self.seating_plan[row][letter]
                if passenger is not None:
                    passenger_data = passenger, f'{row}{letter}'
                    passengers.append(passenger_data)

        return passengers


class Airplane:
    def num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)


class Boeing737(Airplane):
    @staticmethod
    def get_name():  # static method bez self
        return 'Boeing 737'

    @staticmethod
    def seating_plan():
        return range(1, 25), 'ABCDEG'


class AirbusA370(Airplane):
    @staticmethod
    def get_name():
        return 'Airbus A370'

    @staticmethod
    def seating_plan():
        return range(1, 40), 'ABCDEGHJK'


def card_printer(name, seat, plane_model, flight_number):
    text = f'| Pasazer: {name}, Siedzenie: {seat}, Model: {plane_model}, FN: {flight_number} |'
    frame = f'+{"-" * (len(text) - 2)}"+"'
    empty_frame = f'|{"-" * (len(text) - 2)}|'
    border = [frame, empty_frame, text, empty_frame, frame]
    border_text = '\n'.join(border)
    print(border_text)


b = Boeing737()
a = AirbusA370()

f = Flight('BA123', Boeing737())
# print(f.get_airlines())
# print(f.get_number())
# print(f.get_airplane_model())

# print(b.num_seats())
# print(a.num_seats())


f.allocate_passenger('Lech', '1A')
f.allocate_passenger("Jarek K", '24B')
f.allocate_passenger("Krzysztof Jarzyna", '13B')
f.relocate_passenger('13B', '13A')
f.relocate_passenger('13A', '1B')
# pprint(f.seating_plan)
# print(f.num_empty_seats())
f.print_cards(card_printer)  # card printer - parametr dlatego bez nawiasow
