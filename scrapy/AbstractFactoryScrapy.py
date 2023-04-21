import abc
class AbstractFactoryScrapy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_notice_scrapy(self):
        pass

    @abc.abstractmethod
    def create_notices_scrapy(self):
        pass