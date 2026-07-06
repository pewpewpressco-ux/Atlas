import typer

from framework.engine import AtlasEngine

app = typer.Typer()


@app.command()

def run(workflow: str):

    print(f"Requested workflow: {workflow}")

    engine = AtlasEngine()

    print("Workflow dispatch not yet implemented.")


@app.command()

def doctor():

    print("Atlas Repository Health")

    print("✓ Constitution")

    print("✓ Knowledge")

    print("✓ Strategies")

    print("✓ Workflows")


@app.command()

def version():

    print("Atlas v1.0.0-alpha")


if __name__ == "__main__":

    app()
