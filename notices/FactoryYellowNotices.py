from notices.AbstractFactoryNotices import AbstractFactoryNotices
from notices.identityparticulars.IdentityParticulars import IdentityParticulars
class FactoryYellowNotices(AbstractFactoryNotices):
    def create_identity_particulars(self):
        return IdentityParticulars()
    def create_physical_description(self):
        pass
