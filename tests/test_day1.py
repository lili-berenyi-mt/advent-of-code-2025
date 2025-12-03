from advent_of_code_2025.day1 import Dial, InputHandler, turn_dial_as_instructed

def test_turn_dial_left():
    dial = Dial()
    dial.turn_left(5)
    assert dial.get_pointer() == 45

def test_turn_dial_right():
    dial = Dial()
    dial.turn_right(5)
    assert dial.get_pointer() == 55

def test_turn_dial_left_through_0():
    dial = Dial()
    dial.turn_left(55) 
    assert dial.get_pointer() == 95

def test_turn_dial_left_though_100():
    dial = Dial()
    dial.turn_right(55) 
    assert dial.get_pointer() == 5

def test_turn_dial_left_by_1111():
    dial = Dial()
    dial.turn_left(1111) 
    assert dial.get_pointer() == 39

def test_turn_dial_right_by_1111():
    dial = Dial()
    dial.turn_right(1111) 
    assert dial.get_pointer() == 61

def test_get_zero_count_no_turns():
    dial = Dial()
    assert dial.get_zero_count() == 0

def test_get_zero_count_after_turn():
    dial = Dial()
    dial.turn_left(50)
    assert dial.get_zero_count() == 1

def test_get_zero_count_after_multiple_turns():
    dial = Dial()
    dial.turn_left(50)
    dial.turn_right(100)
    dial.turn_left(100)
    assert dial.get_zero_count() == 3

def test_reads_input_from_file():
    inputHandler = InputHandler()
    input = inputHandler.read_input("inputs/day1_test.txt")
    assert input == f"L68\nL30\nR48"

def test_converts_input_into_instruction_list():
    pass
    inputHandler = InputHandler()
    input = inputHandler.read_input("inputs/day1_test.txt")
    instructions = inputHandler.string_to_instruction_list(input)

    assert instructions == [("L",68), ("L",30),("R",48)]

def test_turn_dial_as_instructed():
    dial = Dial()
    instructions = [
        ("L",68),
        ("L",30),
        ("R",48),
        ("L",5),
        ("R",60),
        ("L",55),
        ("L",1),
        ("L",99),
        ("R",14),
        ("L",82),
        ]
    
    code = turn_dial_as_instructed(dial, instructions)
    assert dial.get_zero_count() == 6