from notices.AbstractFactoryNotices import AbstractFactoryNotices
from notices.InterfaceDetails import InterfaceDetails
from notices.InterfaceIdentityParticular import InterfaceIdentityParticular
from notices.InterfacePerson import InterfacePerson
from notices.InterfacePhysicalDescription import InterfacePhysicalDescription

class FactoryYellowNotices(AbstractFactoryNotices):
    def create_identity_particulars(self):
        return InterfaceIdentityParticular()
    def create_physical_description(self):
        return InterfacePhysicalDescription()
    def create_details(self):
        return InterfaceDetails()
    def create_person(self):
        return InterfacePerson()