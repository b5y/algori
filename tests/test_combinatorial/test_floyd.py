import pytest
from algori.combinatorial.floyd import floyd


@pytest.fixture()
def sequence():
    return [2, 0, 6, 3, 1, 6, 3, 1, 6, 3, 1]


def test_floyd():
    assert sequence[floyd(sequence)[0]:floyd(sequence)[0] + floyd(sequence)[1] + 1] == [6, 3, 1]
