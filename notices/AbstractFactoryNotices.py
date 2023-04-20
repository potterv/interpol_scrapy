import abc


class AbstractFactoryNotices(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_identity_particulars(self):
        pass
    @abc.abstractmethod
    def create_physical_description(self):
        pass