import pytest

from pelican.tests.support import temporary_folder


@pytest.fixture
def tmp_folder():
    with temporary_folder() as tf:
        yield tf
