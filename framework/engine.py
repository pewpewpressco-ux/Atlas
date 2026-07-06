from framework.logging import info


class AtlasEngine:

    def __init__(self):

        info("Atlas initialized.")

    def run(self, workflow):

        info(f"Running {workflow.name}")

        workflow.execute()

        info("Workflow complete.")
