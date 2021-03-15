from pprint import pprint

from flight import Flight
from planes import *
from helpers import *


def make_flights():

    f = Flight('BA123', Boeing737())

    f.allocate_passenger('Mike', '1A')
    f.allocate_passenger("John", '24B')
    f.allocate_passenger("Krzysztof Jarzyna", '13B')
    f.relocate_passenger('13B', '13A')
    f.relocate_passenger('13A', '1B')

    pprint(f.seating_plan)

    f.print_cards(card_printer)


if __name__ == '__main__':
    make_flights()
