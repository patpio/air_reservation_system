from airplane import Airplane


class Boeing737(Airplane):
    @staticmethod
    def get_name():
        return 'Boeing 737'

    @staticmethod
    def seating_plan():
        return range(1, 25), 'ABCDEG'
