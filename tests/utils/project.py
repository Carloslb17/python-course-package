 
import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

import cookiecutter
import pytest

from tests.const import PROJECT_DIR


def generate_project(template_values: Dict[str, str]):
    template_values: Dict[str, str] = deepcopy(template_values)
    cookiecutter_config =  {"default_context": template_values}
    cookiecutter_config_fpath = PROJECT_DIR / "tests/cookiecutter.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))
    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR/ "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
        "--verbose"
         ]
    print("COMMAND:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    
    return PROJECT_DIR / "sample" / template_values["repo_name"]
    
