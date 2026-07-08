from framework.artifacts.artifact import Artifact


class ArtifactValidator:

    REQUIRED = [

        "id",

        "title",

        "type"

    ]

    def validate(self, artifact: Artifact):

        for field in self.REQUIRED:

            if getattr(artifact, field) is None:

                raise ValueError(

                    f"{field} missing."

                )

        return True
