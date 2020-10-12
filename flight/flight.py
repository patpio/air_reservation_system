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