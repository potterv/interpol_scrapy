import abc
class AbstractDetails(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_details(self):
        pass