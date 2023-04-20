import abc


class AbstractIdentityParticulars(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getIdentityParticularsr(self):
        pass

    def setIdentityParticularsr(self):
        pass