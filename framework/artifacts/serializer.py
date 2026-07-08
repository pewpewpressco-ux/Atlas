from dataclasses import asdict

import yaml


class ArtifactSerializer:

    def dump(self, artifact):

        return yaml.safe_dump(

            asdict(artifact),

            sort_keys=False

        )
