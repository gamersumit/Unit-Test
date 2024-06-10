import pytest

# pytest -rP    (Print statement will be shown)
# pytest foldername   (particular folder)
# pytest foldername/*.py (particular file)
# pytest foldername/*.py/test_name (particular test)

# Fixture : a fixture is a piece of setup code that is executed before a test function is run. It provides a fixed baseline for the test, ensuring that the test environment is in a known state before the test begins. Fixtures are used to:
# Set Up Test Data: They can create or prepare data structures, objects, or resources needed for the test.
# Set Up Environment: They can configure the test environment, such as setting up databases, initializing services, or mocking external dependencies.
# Clean Up After Tests: Optionally, fixtures can also perform cleanup tasks after the test completes, such as closing connections or releasing resources.

# marks : metadata for test
#  @pytest.mark.skip : to skip a test when needed


@pytest.fixture
def fixture_1():
    # default behaviour : runs each time for secified test
    print('run-fixture-1')
    return 1

@pytest.fixture
def fixture_2(scope = "session"):
    # default behaviour : runs only once per session
    print('run-fixture-2')
    return 2

def test_fixture_1_example_1(fixture_1):
    print('run-exmaple-1')
    num = fixture_1
    assert num == 1

def test_example1(fixture_2):
    print("equal test 1")
    assert 1 == 1


@pytest.mark.xfail
def test_example2():
    assert 1 == 2


@pytest.mark.skip
def test_example3():
    print("skip mark")
    assert 1 == 2


@pytest.fixture
def yield_fixture():
    print('Start Test Phase')
    yield 6
    print('End Test Phase')


def test_example_yield_1(yield_fixture):
    print('run_yeild-example-1')
    assert yield_fixture == 6