from src.cfg_construction import Jump


class InvalidJumpTargetException(Exception):
    def __init__(self, jump: Jump) -> None:
        self._jump = jump
        message = f"invalid target line for jump: {jump.target}"
        super().__init__(message)

    @property
    def jump(self) -> Jump:
        return self._jump

    @jump.setter
    def jump(self, new_jump: Jump) -> None:
        self._jump = new_jump
