import numpy as np
import re

class Solver:
    def __init__(self):
        input = open("Day06/input.txt").readlines()
        matrix = []
        self.sheet = np.array(self.detect_columns(input))
        print(self.sheet)

    def detect_columns(self, lines):
        # find all positions where a digit appears below a space = column start
        col_starts = []
        width = max(len(l) for l in lines)

        for i in range(width):
            if any(l[i] != ' ' for l in lines):
                if i == 0 or all(l[i-1] == ' ' for l in lines):
                    col_starts.append(i)
        col_starts.append(width)  # end

        # slice each line
        result = []
        for line in lines:
            row = [
                line[col_starts[j]:col_starts[j+1]].rstrip('\n')
                for j in range(len(col_starts)-1)
            ]
            result.append(row)
        return result

    
    def solve(self):
        def solve_problem(a):
            operation = a[-1].replace(" ", "")
            numbers = np.array(a[:-1], dtype=np.longlong)
            if operation == '+':
                return np.sum(numbers)
            elif operation == '*':
                return np.prod(numbers)
        solutions = np.apply_along_axis(solve_problem, 0, self.sheet)
        return(np.sum(solutions))
    
    def solve2(self):
        def solve_problem(a):
            operation = a[-1].replace(" ", "")
            numbers = format_problem(a[:-1])
            print(numbers)
            if operation == '+':
                return np.sum(numbers)
            elif operation == '*':
                return np.prod(numbers)
            
        def format_problem(a):
            num_len = len(a[0])
            formatted_numbers = []
            for i in range(num_len):
                num = ''.join([n[i].rstrip(' ') for n in a])
                formatted_numbers.append(num)
            return np.array(list(filter(None, formatted_numbers)), dtype=np.longlong)

        solutions = np.apply_along_axis(solve_problem, 0, self.sheet)
        print(solutions)
        return(np.sum(solutions))



solver = Solver()
print(solver.solve2())