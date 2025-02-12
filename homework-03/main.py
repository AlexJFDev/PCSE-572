from math import pi
import math
import numpy as np

from rotation import Rotation
from quaternion import Quaternion
from transform import Transformation

ANGLES = [pi / 2, pi / 3, pi / 4, pi / 6, -pi / 3, -pi / 6]
AXES = ["x", "y", "z"]

if __name__ == "__main__":
    for angle in ANGLES:
        print(f"Angle: {angle}")
        for axis in AXES:
            print(f"\tAxis: {axis}")
            rotation = Rotation(axis=axis, angle=angle)
            print("\t\tRotation Matrix:")
            r_str = str(rotation.rotation_matrix.round(decimals=2)).replace("\n", "\n\t\t\t")
            print(f"\t\t\t{r_str}")
            print("\t\tRotation Quaternion")
            print(f"\t\t\t{rotation.rotation_quaternion.component_array.round(decimals=2)}")
        print()

    quaternion = Quaternion(0.74846, 0.13062, 0.50764, 0.40626)
    rotation = Rotation(rotation_quaternion=quaternion)
    print(rotation.rotation_matrix.round(decimals=3))

    # pelvis -> waist
    translation_pelvis_waist = (0., 0., 0.137)
    rotation_pelvis_waist = Rotation(rotation_quaternion=(1., 0., 0., 0.))
    transformation_pelvis_waist = Transformation(translation_pelvis_waist, rotation_pelvis_waist)
    # waist -> torso
    translation_waist_torso = (0., 0., 0.)
    rotation_waist_torso = Rotation(rotation_quaternion=(1., 0., 0.003, 0.))
    transformation_waist_torso = Transformation(translation_waist_torso, rotation_waist_torso)
    # torso -> shoulder pitch
    translation_torso_shoulder_pitch = (0., -0.234, 0.165)
    rotation_torso_shoulder_pitch = Rotation(rotation_quaternion=(0.851, 0., -0.525, 0.))
    transformation_torso_shoulder_pitch = Transformation(translation_torso_shoulder_pitch, rotation_torso_shoulder_pitch)
    # shoulder pitch -> shoulder roll
    translation_shoulder_pitch_shoulder_roll = (0., 0., 0.)
    rotation_shoulder_pitch_shoulder_roll = Rotation(rotation_quaternion=(0.96, -0.279, 0., 0.))
    transformation_shoulder_pitch_shoulder_roll = Transformation(translation_shoulder_pitch_shoulder_roll, rotation_shoulder_pitch_shoulder_roll)
    # shoulder roll -> shoulder yaw
    translation_shoulder_roll_shoulder_yaw = (0., 0., 0.)
    rotation_shoulder_roll_shoulder_yaw = Rotation(rotation_quaternion=(0.842, 0., 0., 0.54))
    transformation_shoulder_roll_shoulder_yaw = Transformation(translation_shoulder_roll_shoulder_yaw, rotation_shoulder_roll_shoulder_yaw)
    # shoulder yaw -> elbow
    translation_shoulder_yaw_elbow = (0.03, 0., -0.246)
    rotation_shoulder_yaw_elbow = Rotation(rotation_quaternion=(0.863, 0., -0.506, 0.))
    transformation_shoulder_yaw_elbow = Transformation(translation_shoulder_yaw_elbow, rotation_shoulder_yaw_elbow)
    # elbow -> wrist yaw
    translation_elbow_wrist_yaw = (-0.03, 0., -0.186)
    rotation_elbow_wrist_yaw = Rotation(rotation_quaternion=(0.566, 0., 0., 0.824))
    transformation_elbow_wrist_yaw = Transformation(translation_elbow_wrist_yaw, rotation_elbow_wrist_yaw)
    # wrist yaw -> wrist roll
    translation_wrist_yaw_wrist_roll = (0., 0., 0.)
    rotation_wrist_yaw_wrist_roll = Rotation(rotation_quaternion=(0.904, -0.428, 0., 0.))
    transformation_wrist_yaw_wrist_roll = Transformation(translation_wrist_yaw_wrist_roll, rotation_wrist_yaw_wrist_roll)
    # wrist roll -> hand
    translation_wrist_roll_hand = (0., 0., 0.)
    rotation_wrist_roll_hand = Rotation(rotation_quaternion=(0.797, 0., 0., -0.605))
    transformation_wrist_roll_hand = Transformation(translation_wrist_roll_hand, rotation_wrist_roll_hand)
    # hand -> palm
    translation_hand_palm = (0., 0., -0.16)
    rotation_hand_palm = Rotation(rotation_quaternion=(0., 0.707, 0.707, 0.))
    transformation_hand_palm = Transformation(translation_hand_palm, rotation_hand_palm)

    transformation_pelvis_palm = transformation_pelvis_waist * transformation_waist_torso * transformation_torso_shoulder_pitch * transformation_shoulder_pitch_shoulder_roll * transformation_shoulder_roll_shoulder_yaw * transformation_shoulder_yaw_elbow * transformation_elbow_wrist_yaw *transformation_wrist_yaw_wrist_roll * transformation_wrist_roll_hand * transformation_hand_palm
    
    contact_point = np.array([0., 0., 0.2, 1.])
    print(transformation_pelvis_palm.transformation_matrix @ contact_point)