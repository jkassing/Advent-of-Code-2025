from math import floor

class Solver:
    def __init__(self, input_file):
        self.inputs = open(input_file).read().strip().splitlines()
        self.pos = 50
        self.code = 0

    def rotate(self, direction, amount):
        rest = amount % 100
        unnormalized_pos = self.pos + rest if direction == "R" else self.pos - rest
        extra = 1 if((self.pos != 0 and unnormalized_pos <= 0) or (unnormalized_pos > 99)) else 0
        if direction == "R":
            self.pos = (self.pos + amount) % 100
        else:
            self.pos = (self.pos - amount) % 100
        self.code += floor(amount / 100) + extra

    def solve(self):
        for line in self.inputs:
            direction = line[0]
            amount = int(line[1:])
            self.rotate(direction, amount)
        return self.code


solver = Solver("Day01/input.txt")
print(solver.solve())
