from airplane import Airplane


class AirbusA370(Airplane):
    @staticmethod
    def get_name():
        return 'Airbus A370'

    @staticmethod
    def seating_plan():
        return range(1, 40), 'ABCDEGHJK'
