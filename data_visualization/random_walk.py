from random import choice

class RandomWalk:
    """A class to genderate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points


        # All walks start at (0, 0)
        self.x_vals = [0]
        self.y_vals = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_vals) < self.num_points:
            # Decide which direction to go and how far to go
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_vals[-1] + x_step
            next_y = self.y_vals[-1] + y_step

            self.x_vals.append(next_x)
            self.y_vals.append(next_y)