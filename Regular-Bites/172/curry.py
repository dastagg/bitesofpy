from functools import partial


# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places
def rounder(x, places):
    return round(x, places)


rounder_int = partial(rounder, places=0)
rounder_detailed = partial(rounder, places=4)
