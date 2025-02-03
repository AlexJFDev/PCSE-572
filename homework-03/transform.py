from rotation import Rotation
import numpy as np

class Transformation:
    translation: np.ndarray[float, float]
    rotation: Rotation
    transformation_matrix: np.ndarray[float, float]

    def __init__(self, translation: tuple[float, float, float], rotation: Rotation) -> None:
        self.translation = np.array(translation)
        self.rotation = rotation

        partial_transform = np.vstack(self.rotation.rotation_matrix, self.translation)
        self.transformation_matrix = np.hstack((partial_transform, np.array([0, 0, 0, 1])))
        
        def __mul__(self, other):
            new_transformation = self.transformation_matrix @ other.transformation_matrix
            new_translation = new_transformation[:3, 3]
            new_rotation = Rotation(new_transformation[:3, :3])
            return Transformation(new_translation, new_rotation)