
class Solver(object):
    def __init__(self, input_file):
        self.inputs = open(input_file).read().strip().splitlines()[0].split(',')
        print(self.inputs)
        self.invalid_sum = 0

    
    def solve(self, part):
        for interval in self.inputs:
            if part == 2:
                self.check_range2(interval.split('-'))
            else:   
                self.check_range(interval.split('-'))
        return self.invalid_sum

    def check_range(self, interval: str):
        for number in range(int(interval[0]), int(interval[1]) + 1):
            s = str(number)
            length = len(s)
            half = length // 2
            if length % 2 == 0 and s[:half] == s[half:]:
                self.invalid_sum += number

    def check_range2(self, interval: str):
        for number in range(int(interval[0]), int(interval[1]) + 1):
            s = str(number)
            length = len(s)
            for k in range(1, (length // 2) + 1):
                if (length % k != 0):
                    continue
                # check if substring repeated k times is the og string
                if s == s[:k] * (length // k):
                    self.invalid_sum += number
                    break


solver = Solver("Day02/input.txt")
print(solver.solve(part=2))
