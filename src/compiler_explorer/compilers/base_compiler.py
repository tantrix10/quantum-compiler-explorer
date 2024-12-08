from abc import abstractmethod


class Program:
    pass


class BaseCompiler:

    def __init__(self) -> None:
        pass

    @abstractmethod
    def placement(self, program, architecture=None, calibration=None):
        pass

    @abstractmethod
    def routing(self, program, architecture=None, calibration=None):
        pass

    @abstractmethod
    def optimisation(self, program, architecture=None, calibration=None):
        pass

    @abstractmethod
    def optimal_compilation(self, program, architecture=None, calibration=None):
        pass