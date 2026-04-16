from sample import insecure_function


def test_insecure_function():
    insecure_function()
    assert False  # Intentional failure