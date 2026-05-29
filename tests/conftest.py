from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    original_activities = deepcopy(activities)

    # Arrange: start each test from the same in-memory state.
    activities.clear()
    activities.update(deepcopy(original_activities))

    yield

    # Cleanup: restore original values after each test.
    activities.clear()
    activities.update(deepcopy(original_activities))
