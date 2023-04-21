from notices.AbstractPerson import AbstractPerson
from notices.person.Person import Person


class InterfacePerson(AbstractPerson):
    def interface_person(self):
        return Person()