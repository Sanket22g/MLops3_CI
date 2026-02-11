import pytest

def square(x):
    return x * x

def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0

if __name__ == "__main__":
    pytest.main()

def test_invalid_input():
    with pytest.raises(TypeError):
        square("a string")

        