import math
import numpy as np

class Quaternion:
    def __init__(self, w, x, y, z):
        self.component_array = np.array([w, x, y, z])

    def copy(self):
        return Quaternion(self.component_array[0], self.component_array[1], self.component_array[2], self.component_array[3])