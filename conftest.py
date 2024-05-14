import logging

import pytest

log = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def capture_test_name(request):
    test_name = request.node.name
    return test_name