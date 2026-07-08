"""
Atlas Runtime Kernel

This is the central operating system for Atlas.

No workflow, department, or service should directly manipulate the
repository. Everything flows through the Atlas runtime.
"""

from framework.librarian import Librarian
from framework.knowledge import KnowledgeGraph
from framework.logging import info


class Atlas:

    def __init__(self):

        self.librarian = Librarian()

        self.graph = KnowledgeGraph()

        self.departments = {}

        self.context = {}

    def register_department(self, name, department):

        self.departments[name] = department

    def run_department(self, name):

        info(f"Running Department: {name}")

        return self.departments[name].run(self)

    def remember(self, artifact):

        self.librarian.register(artifact)

    def relate(self, parent, child, relationship):

        self.graph.relate(

            parent,

            child,

            relationship

        )

    def load_memory(self):

        info("Loading institutional memory.")

    def save(self):

        info("Saving repository state.")
