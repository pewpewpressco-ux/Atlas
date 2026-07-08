from framework.artifacts.artifact import Artifact


class ArtifactFactory:

    def create(

        self,

        identifier,

        title,

        artifact_type,

        **kwargs

    ):

        return Artifact(

            id=identifier,

            title=title,

            type=artifact_type,

            **kwargs

        )
