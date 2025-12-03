class Dial:
    def __init__(self):
        self.pointer = 50
        self.zero_count = 0

    def get_pointer(self):
        return self.pointer
    
    def set_pointer(self, value):
        self.pointer = value
        if value == 0:
            self.zero_count += 1 
    
    def get_zero_count(self):
        return self.zero_count

    def turn_left(self, amount):
        while amount > 0:
            if self.pointer == 0:
                self.set_pointer(99)
            else:
                self.set_pointer(self.pointer-1)
            amount -= 1

    def turn_right(self, amount):
        while amount > 0:
            if self.pointer == 99:
                self.set_pointer(0)
            else:
                self.set_pointer(self.pointer+1)
            amount -= 1


class InputHandler:
    def read_input(self, location):
        f = open(location)
        input = f.read()
        return input
    
    @staticmethod
    def _string_to_instruction(input):
        return (input[0], int(input[1:]))
    
    def string_to_instruction_list(self, input): 
        instruction_strings = input.split(f"\n")
        instructions = map(InputHandler._string_to_instruction, instruction_strings)
        return list(instructions)
    
def turn_dial_as_instructed(dial, instructions):
    for i in instructions:
        if i[0] == "L":
            dial.turn_left(i[1])
        else:
            dial.turn_right(i[1])

    return dial.get_zero_count()

if __name__ == "__main__":
    dial = Dial()
    inputHandler = InputHandler()
    input = inputHandler.read_input("inputs/day1.txt")
    instructions = inputHandler.string_to_instruction_list(input)
    turn_dial_as_instructed(dial, instructions)
    password = dial.get_zero_count()
    print(f"The password is: {password}")