
class Solver(object):
    def __init__(self, input_file):
        self.inputs = open(input_file).read().strip().splitlines()[0].split(',')
        print(self.inputs)
        self.invalid_sum = 0

    
    def solve(self):
        for interval in self.inputs:
            self.check_range2(interval.split('-'))
        return self.invalid_sum

    def check_range(self, interval: str):
        for number in range(int(interval[0]), int(interval[1]) + 1):
            stringNumber = str(number)
            length = len(stringNumber)
            if (length % 2 != 0):
                continue
            left = stringNumber[:length // 2]
            right = stringNumber[length // 2:]
            if left == right:
                self.invalid_sum += number

    def check_range2(self, interval: str):
        for number in range(int(interval[0]), int(interval[1]) + 1):
            stringNumber = str(number)
            length = len(stringNumber)
            for k in range(1, (length // 2) + 1):
                if (length % k != 0):
                    continue
                if stringNumber == stringNumber[:k] * (length // k):
                    self.invalid_sum += number
                    break


solver = Solver("Day02/input.txt")
print(solver.solve())
