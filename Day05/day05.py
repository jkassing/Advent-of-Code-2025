
class Solver:
    def __init__(self):
        input = open('Day05/input.txt').read().strip().split('\n\n')
        self.ranges = [tuple(map(int, i.split('-'))) for i in input[0].splitlines()]
        self.ingredients = list(map(int, input[1].splitlines()))
        self.fresh_count = 0
        self.tmp_array = []

    def solve(self):
        print(len(self.ingredients))
        for ingredient in self.ingredients:
            self.check_freshness(ingredient)
        print(self.fresh_count)
    
    def check_freshness(self, ingredient):
        for range in self.ranges:
            if range[0] <= ingredient <= range[1]:
                self.fresh_count += 1
                return
            
    def solve2(self):
        combined_any = True
        while combined_any:
            combined_any = False
            for r in self.ranges:
                if not self.tmp_array:
                    self.tmp_array.append(r)
                    continue
                if self.combine_ranges(r):
                    combined_any = True
            self.ranges = self.tmp_array
            self.tmp_array = [] 
        num_fresh_ingredients = sum([y-x+1 for (x,y) in self.ranges])
        print(num_fresh_ingredients)

    def combine_ranges(self, range):
        startNew, endNew = range
        for i,( startOld, endOld) in enumerate(self.tmp_array):
            if startNew < startOld:
                if endNew < startOld:
                    continue
                if endNew >= endOld:
                    self.tmp_array[i] = (startNew, endNew)
                    return True
                if endNew <= endOld:
                    self.tmp_array[i] = (startNew, endOld)
                    return True
            if startOld <= startNew <= endOld:
                if endNew <= endOld:
                    return True
                if endNew > endOld:
                    self.tmp_array[i] = (startOld, endNew)
                    return True
            if startNew > endOld:
                continue
        self.tmp_array.append((startNew, endNew))
        return False


solver = Solver()
solver.solve()
solver.solve2()