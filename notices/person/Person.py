class Person:
    __id_person: str
    __link: str
    @property
    def id_person(self):
        return self.__id_person
    @id_person.setter
    def id_person(self, id_person):
        self.__id_person = id_person
    @property
    def link(self):
        return self.__link
    @link.setter
    def link(self, link):
        self.__link = link