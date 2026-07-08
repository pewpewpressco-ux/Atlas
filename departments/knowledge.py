from framework.services.librarian import LibrarianService

from framework.services.archive import ArchiveManager


class KnowledgeDepartment(Department):

    name = "Knowledge"

    def run(self, atlas):

        LibrarianService().run(atlas)

        ArchiveManager().run(atlas)
