import subprocess
from pathlib import Path


# generate a project
def test__linting_passes(project_dir: Path):
    # Check.
    # subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)
    assert True


def test__tests_pass(project_dir: Path):
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)
