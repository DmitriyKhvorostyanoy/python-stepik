import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^")
    yield
    print(":3")


@pytest.fixture()
def very_important_fixture():
    print(":)")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print()

    def test_second_smiling_faces(self, prepare_faces):
        print()
