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
        row_new, letter_new = self._parse_seat(seat_to)

        self.check_place(row_new, letter_new, seat_to)
        self.seating_plan[row_new][letter_new] = self.seating_plan[row_old][letter_old]
        self.seating_plan[row_old][letter_old] = None


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
pprint(f.seating_plan)
