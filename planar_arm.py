import math

"""A class for a PlanarArm with any number of segments. Not all methods are fully implemented."""
class PlanarArm:
    def __init__(self, segment_lengths: list[float]):
        self.segment_lengths = segment_lengths
        self.total_segments = len(segment_lengths)

    def calculate_end_effector_position(self, joint_angles: list[float]):
        x, y, angle_sum = 0
        for i in range(self.total_segments):
            angle_sum += joint_angles[i]
            x += math.cos(angle_sum) * self.segment_lengths[i]
            y += math.sin(angle_sum) * self.segment_lengths[i]
        return x, y
    
    def calculate_segment_angles(self, end_effector_position: tuple[float, float]):
        x, y = end_effector_position
        if self.total_segments == 1:
            raise NotImplementedError
        elif self.total_segments == 2:
            if (not self.is_reachable(end_effector_position)):
                raise ValueError
            length1 = self.segment_lengths[0]
            length2 = self.segment_lengths[1]

            angle_2 = math.acos(
                (x ** 2 + y ** 2 - length1 ** 2 - length2 ** 2) /
                (2 * length1 * length2)
            )

            angle_1a = math.atan2(y, x) - math.atan2(length2 * math.sin(angle_2), length1 + length2 * math.cos(angle_2))
            angle_1b = math.atan2(y, x) - math.atan2(length2 * math.sin(-angle_2), length1 + length2 * math.cos(-angle_2))

            return (angle_1a, angle_2), (angle_1b, -angle_2)
        else:
            raise NotImplementedError

    def is_reachable(self, position: tuple[float, float]):
        x, y = position
        radial_distance = math.sqrt(x ** 2 + y ** 2)
        if self.total_segments == 1:
            raise NotImplementedError
        elif self.total_segments == 2:
            length_1 = self.segment_lengths[0]
            length_2 = self.segment_lengths[1]
            r_min = abs(length_1 - length_2)
            r_max = length_1 + length_2

            return r_min <= radial_distance <= r_max