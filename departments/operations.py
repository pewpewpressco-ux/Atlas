from framework.services.portfolio import PortfolioManager

from framework.services.performance import PerformanceReview


class OperationsDepartment(Department):

    name = "Operations"

    def run(self, atlas):

        PortfolioManager().run(atlas)

        PerformanceReview().run(atlas)
