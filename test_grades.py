import pytest

from grades import is_pass, result


@pytest.mark.parametrize(
    "score, expected",
    [
        (90, True),
        (50, True),  # Exact pass boundary
        (49, False),  # Just below pass boundary
        (20, False),
    ],
)
def test_is_pass(score: int, expected: bool) -> None:
    assert is_pass(score) == expected


@pytest.mark.parametrize(
    "score, expected",
    [
        (90, "Pass"),
        (50, "Pass"),
        (49, "Fail"),
        (20, "Fail"),
    ],
)
def test_result(score: int, expected: str) -> None:
    assert result(score) == expected
