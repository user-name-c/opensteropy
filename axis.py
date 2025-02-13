import numpy as np
from .dipdir import Dipdir

class Axis:
    def __init__(self, dip_dir, dip):
        self.dip_dir = dip_dir
        self.dip = dip
        self.vector = self.to_vector()

    def to_vector(self):
        return Dipdir(self.dip_dir, self.dip).to_vector()

