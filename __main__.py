from pprint import pprint

from flight import Flight
from planes import *
from helpers import *


def make_flights():
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


if __name__ == '__main__':
    make_flights()
