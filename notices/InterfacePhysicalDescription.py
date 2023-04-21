from notices.AbstractPhysicalDescription import AbstractPhysicalDescription
from notices.physicaldescription.PhysicalDescription import PhysicalDescription


class InterfacePhysicalDescription(AbstractPhysicalDescription):
    def interface_physical_description(self):
        return PhysicalDescription()