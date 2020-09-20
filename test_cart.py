
import pytest
from myCart import run

pytest_plugins = ["pytester"]

@pytest.fixture
def run(testdir):
    def do_run(*args):
        args = ["pyconv"] + list(args)
        return testdir._run(*args)
    return do_run

    def test_run():
        run()