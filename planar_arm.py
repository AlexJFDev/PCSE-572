import math

class PlanarArm:
    def __init__(self, arm_lengths: list[float]):
        self.arm_lengths = arm_lengths
        self.arms = len(arm_lengths)

    def calculate_end_effector_position(self, joint_angles: list[float]):
        x, y, angle_sum = 0
        for i in range(self.arms):
            angle_sum += joint_angles[i]
            x += math.cos(angle_sum) * self.arm_lengths[i]
            y += math.sin(angle_sum) * self.arm_lengths[i]
        return x, y
    
    def calculate_arm_angles(self, end_effector_position: tuple[float, float]):
        if self.arms == 1:
            raise NotImplementedError
        elif self.arms == 2:
            raise NotImplementedError
        elif self.arms == 3:
            raise NotImplementedError
        else:
            raise NotImplementedError