import numpy as np
from .plane import Plane
from .axis import Axis

def rotate_plane(plane, axis, angle):
    """Rota un plano alrededor de un eje usando la fórmula de Rodrigues."""
    axis_vextor = axis.to_vector()
    pole_vector = plane.vector_pole()
    pole_vector_rot = rotate_vector(pole_vector, axis_vextor, -angle)
    plane_rot = Plane.from_vector_pole(pole_vector_rot)
    return plane_rot

def rotate_line(line, axis, angle):
    axis_vextor = axis.to_vector()
    line_vector = line.to_vector()
    line_vector_rot = rotate_vector(line_vector, axis_vextor, -angle)
    line_rot = Axis.from_vector(line_vector_rot)
    return line_rot

def rotate_vector(vector, axis, angle):
    angle = np.radians(angle)
    axis = axis / np.linalg.norm(axis)  # Asegurar que el eje es unitario
    v_rot = (vector * np.cos(angle) +
             np.cross(axis, vector) * np.sin(angle) +
             axis * np.dot(axis, vector) * (1 - np.cos(angle)))
    return v_rot