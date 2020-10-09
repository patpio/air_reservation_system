from pprint import pprint


class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

        rows, seats = self.airplane.seating_plan()
        self.seating_plan = [None]+[{seat: None for seat in seats} for _ in rows]

    def get_airlines(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.airplane.get_name()

    def _parse_seat(self,seat):
        rows, seats = self.airplane.seating_plan()
        letter = seat[-1]
        if letter not in seats:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text=seat[:-1]

        try:
            row=int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row number {row_text}')

        if row not in rows:
            raise ValueError(f'Row number is out of range {row}')

        return row, letter

    def allocate_passenger(self, passenger='Pat P', seat='12C'):
        row, letter =self._parse_seat(seat)

        if self.seating_plan[row][letter] is not None:
            raise ValueError(f'Seat is already taken {seat}')
        self.seating_plan[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):
        pass



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

pprint(f.seating_plan)
