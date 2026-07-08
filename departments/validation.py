from framework.services.critic import Critic

from framework.services.backtesting import Backtester

from framework.services.promotion import PromotionReview


class ValidationDepartment(Department):

    name = "Validation"

    def run(self, atlas):

        Critic().run(atlas)

        Backtester().run(atlas)

        PromotionReview().run(atlas)
