from advent_of_code_2025.day2 import InputHandler, PatternFinder, get_pattern_total

def test_reads_input_from_file():
    input = InputHandler.read_input("inputs/day2_test.txt")
    assert input == "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def test_gets_ranges_from_input():
    input = "11-22,95-115,998-1012"
    ranges = InputHandler.get_ranges(input)
    assert ranges == [(11,22), (95,115),(998,1012)]

def test_get_pattern_count_from_range():
    range = (1188511880,1188511890)
    patternFinder = PatternFinder(range)
    patterns = patternFinder.find_patterns()
    assert patterns == [1188511885]

def test_has_correct_sum():
    input = InputHandler.read_input("inputs/day2_test.txt")
    ranges = InputHandler.get_ranges(input)
    sum = get_pattern_total(ranges)
    assert sum == 1227775554