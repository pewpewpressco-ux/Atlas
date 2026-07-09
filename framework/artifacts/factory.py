from framework.artifacts.artifact import Artifact
from framework.artifacts.enums import ArtifactType


class ArtifactFactory:

    def create(
        self,
        identifier,
        title,
        artifact_type: ArtifactType,
        **kwargs,
    ) -> Artifact:
        return Artifact(
            id=identifier,
            title=title,
            type=artifact_type,
            **kwargs,
        )
