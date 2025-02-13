import numpy as np
from .dipdir import Dipdir

class Plane:
    def __init__(self, dip_dir, dip):
        self.dip_dir = dip_dir
        self.dip = dip

    def to_pole(self):
        dip = 90 - self.dip
        dip_dir = self.dip_dir + 180
        if dip_dir > 360:
            dip_dir -= 360
        return dip_dir, dip

    def vector_pole(self):
        dip_dir, dip = Plane.to_pole(self)
        vector = Dipdir(dip_dir, dip).to_vector()
        return vector

    @staticmethod
    def from_vector_pole(vector):
        dip_dir, dip = Dipdir.from_vector(vector)
        return Plane(*Plane.pole_to_plane(dip_dir, dip))

    @staticmethod
    def pole_to_plane(dip_dir, dip):
        dip = 90 - dip
        dip_dir -= 180
        if dip_dir < 0:
            dip_dir += 360
        return dip_dir, dip

    def to_strike(self):
        strike = self.dip_dir - 90
        if strike < 0:
            strike += 360
        return strike, self.dip

    @staticmethod
    def from_strike(strike, dip):
        dip_dir = strike + 90
        if dip_dir > 360:
            dip_dir -= 360
        return Plane(dip_dir, dip)