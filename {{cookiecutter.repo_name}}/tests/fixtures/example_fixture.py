from uuid import uuid4

import pytest

from tests.const import PROJECT_DIR


@pytests.fixture(scope="session")
def test_session_id() -> str:
    test_session_id = str(uuid4())[:6]
    return test_session_id