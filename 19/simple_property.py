"""Promo class."""
from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires


    @property
    def expired(self):
        if self.expires <= NOW:
            return True
        else:
            return False

