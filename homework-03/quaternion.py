import math
import numpy as np

class Quaternion:
    def __init__(self, w, x, y, z):
        self.component_array = np.array([w, x, y, z])