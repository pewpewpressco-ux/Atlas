from pathlib import Path

from framework.artifacts.serializer import ArtifactSerializer


class ArtifactRepository:

    def __init__(self, root):

        self.root = Path(root)

        self.serializer = ArtifactSerializer()

    def save(self, artifact):

        path = self.root / f"{artifact.id}.yaml"

        path.write_text(

            self.serializer.dump(artifact),

            encoding="utf8"

        )

        return path
