import abc


class AbstractPhysicalDescription(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_physical_description(self):
        pass