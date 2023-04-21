import abc
class AbstractPerson(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_person(self):
        pass