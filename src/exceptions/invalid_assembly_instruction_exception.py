

class InvalidAssemblyInstruction(Exception):
    def __init__(self, instruction: any, line: int) -> None:
        self._instruction = instruction
        self._line = line
        message = f"The instruction in line {line} is not a valid assembly instruction: '{instruction}'"
        super().__init__(message)

    @property
    def instruction(self) -> any:
        return self._instruction

    @instruction.setter
    def instruction(self, new_instruction: any) -> None:
        self._instruction = new_instruction

    @property
    def line(self) -> int:
        return self._line

    @line.setter
    def line(self, new_line: int) -> None:
        self._line = new_line
