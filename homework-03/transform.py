from rotation import Rotation
import numpy as np

class Transformation:
    def __init__(self, translation: tuple[float, float, float], rotation: Rotation) -> None:
        self.translation = np.array(translation)
        self.rotation = rotation

        partial_translation = np.vstack(self.rotation.rotation_matrix, self.translation)
        self.translation_matrix = np.hstack((partial_translation, np.array([0, 0, 0, 1])))
        
        