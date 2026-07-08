from framework.departments.base import Department

from framework.services.universe import UniverseDiscovery

from framework.services.regime import RegimeDetection

from framework.services.scientist import ChiefScientist


class ResearchDepartment(Department):

    name = "Research"

    def run(self, atlas):

        UniverseDiscovery().run(atlas)

        RegimeDetection().run(atlas)

        ChiefScientist().run(atlas)
