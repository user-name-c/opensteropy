import numpy as np

class Dipdir:
    def __init__(self, dip_dir, dip):
        self.dip_dir = dip_dir
        self.dip = dip
        self.vector = self.to_vector()
    
    def to_vector(self):
        dip_dir_rad = np.radians(self.dip_dir)
        dip_rad = np.radians(self.dip)
        v_x = np.sin(dip_dir_rad) * np.cos(dip_rad)
        v_y = np.cos(dip_dir_rad) * np.cos(dip_rad)
        v_z = np.sin(dip_rad)
        return np.array([v_x, v_y, v_z])

    @staticmethod
    def from_vector(vector):
        V_x, V_y, V_z = vector
        dip = np.degrees(np.arcsin(V_z))
        dip_dir = np.degrees(np.arctan2(V_x, V_y))
        if dip < 0:
            dip = -dip
            dip_dir -= 180        
        if dip_dir < 0:
            dip_dir += 360  # Asegurar que esté entre 0 y 360°
        return dip_dir, dip

    def normalize(self):
        norm = np.linalg.norm(self.vector)
        if norm != 0:
            self.vector /= norm
        return self 