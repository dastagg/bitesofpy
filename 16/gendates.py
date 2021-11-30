""" This is the gendates module.

Functions
---------
gen_special_pybites_dates()
    Create generator to calculate next date.

"""

from datetime import datetime, timedelta
from itertools import islice
from pprint import pprint as pp

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    """Create generator to calculate next date."""
    days = 0
    while True:
        days += 1
        if days % 100 == 0:
            yield PYBITES_BORN + timedelta(days=days)


def main():
    """This is main."""
    gen = gen_special_pybites_dates()
    # print a couple dates
    pp(next(gen))
    pp(next(gen))
    pp(next(gen))
    pp(next(gen))
    pp(next(gen))

    # print 10 dates, restart the generator
    gen = gen_special_pybites_dates()
    print("Starting from the beginning...")
    pp(list(islice(gen, 10)))

    # print 25 dates, restart the generator
    gen = gen_special_pybites_dates()
    print("Starting from the beginning...")
    pp(list(islice(gen, 25)))


if __name__ == "__main__":
    main()
