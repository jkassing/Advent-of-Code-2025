import numpy as np

class Solver:
    def __init__(self):
        self.grid = self.load_grid('Day04/input.txt')

    def load_grid(self, input_file):
        with open(input_file) as f:
            lines = [list(line.rstrip('\n')) for line in f]
        arr = np.array(lines, dtype=str)
        return (arr == '@')   # boolean array where True = '@'

    def place_forklifts(self):
        g = self.grid.astype(np.int8)
        total_forklifts = 0
        while True:

            # Build a padded grid to avoid boundary checks
            padded = np.pad(g, pad_width=1, mode='constant', constant_values=0)

            # Sum a 3×3 window for all positions using slicing
            window_sum = (
                padded[:-2, :-2] + padded[:-2, 1:-1] + padded[:-2, 2:] +
                padded[1:-1, :-2] + padded[1:-1, 1:-1] + padded[1:-1, 2:] +
                padded[2:, :-2] + padded[2:, 1:-1] + padded[2:, 2:]
            )

            # Only count windows centered on actual '@' cells
            num_forklifts = np.sum((g == 1) & (window_sum <= 4))
            if num_forklifts == 0:
                print(total_forklifts)
                return
            total_forklifts += num_forklifts
            g[(g == 1) & (window_sum <= 4)] = 0
            
            print(num_forklifts)



solver = Solver()
solver.place_forklifts()