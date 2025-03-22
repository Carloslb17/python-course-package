"Generation Project test"

from pathlib import Path


# Make tests concise.
def test__can_generate_project(project_dir: Path):
    """
    execute: "cookiecutter <template directory> ..

    """

    assert project_dir.exists()
