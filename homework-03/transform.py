from rotation import Rotation
import numpy as np

class Transformation:
    translation: np.ndarray[float, float]
    rotation: Rotation
    transformation_matrix: np.ndarray[float, float]

    def __init__(self, translation: tuple[float, float, float], rotation: Rotation) -> None:
        self.translation = np.array(translation)
        self.rotation = rotation

        self.transformation_matrix = np.eye(4)
        self.transformation_matrix[:3, :3] = self.rotation.rotation_matrix
        self.transformation_matrix[:3, 3] = self.translation
        
    def __mul__(self, other):
        new_transformation = self.transformation_matrix @ other.transformation_matrix
        new_rotation = Rotation(rotation_matrix=new_transformation[:3, :3])
        new_translation = new_transformation[:3, 3]
        return Transformation(new_translation, new_rotation)