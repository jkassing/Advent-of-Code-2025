
class Solver:
    def __init__(self):
        self.inputs = open("Day03/input.txt").readlines()
        self.joltage = 0

    def solve(self):
        for bank in self.inputs:
            bank1 = list(bank.strip())
            first_digit_index = max(range(len(bank1) -1), key=lambda x : bank1[x])
            first_digit = bank1[first_digit_index]
            second_digit = max(bank1[first_digit_index+1:])
            joltage = first_digit + second_digit
            self.joltage += int(joltage)
        print(self.joltage)

    def solve2(self):
        for bank in self.inputs:
            digits_left = 12
            joltage = ''
            bank1 = list(bank.strip())
            while(digits_left > 0):
                digit_index = max(range(len(bank1) -digits_left+1), key=lambda x : bank1[x])
                digit = bank1[digit_index]
                joltage += digit
                bank1 = bank1[digit_index+1:]
                digits_left -= 1
            self.joltage += int(joltage)
        print(self.joltage)
        
solver = Solver()
solver.solve2()