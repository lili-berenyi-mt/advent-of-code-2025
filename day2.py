class InputHandler:

    @staticmethod
    def read_input(location):
        f = open(location)
        input = f.read()
        return input
    
    @staticmethod
    def _string_to_range(input_string):
        limit_strings = input_string.split("-")
        range = (int(limit_strings[0]), int(limit_strings[1]))
        return range

    @staticmethod
    def get_ranges(input):
        range_strings = input.split(",")
        ranges = map(InputHandler._string_to_range, range_strings)
        return list(ranges)
    
class PatternFinder:

    def __init__(self, range):
        self.range = range
        self.patterns = []

    @staticmethod
    def _has_odd_digits(number):
        return len(str(number))%2 ==1 
    
    @staticmethod
    def _is_repeated(number):
        number_as_str = str(number)
        half_length = (len(number_as_str)//2)
        first_half = number_as_str[0:half_length]
        second_half = number_as_str[half_length:]
        return first_half==second_half
    
    def find_patterns(self):
        limit = self.range[1]+1
        i = self.range[0]
        while i < limit:
            if PatternFinder._has_odd_digits(i):
                i += 1
                continue
            elif PatternFinder._is_repeated(i):
                self.patterns.append(i)
            i += 1
        return self.patterns
            

def get_pattern_total(ranges):
    total = 0
    for range in ranges:
        patternFinder = PatternFinder(range)
        patterns = patternFinder.find_patterns()
        total += sum(patterns)
    return total

def get_day_2_solution():
    input = InputHandler.read_input("inputs/day2.txt")
    ranges = InputHandler.get_ranges(input)
    solution = get_pattern_total(ranges)
    return solution

if __name__ == '__main__':
    solution = get_day_2_solution()
    print(f"The solution is: {solution}")

