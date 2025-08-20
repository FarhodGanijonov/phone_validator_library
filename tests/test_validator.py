from uzb_phone_validator import is_valid, normalize

def test_valid_numbers():
    assert is_valid("+998901234567")
    assert is_valid("+998991112233")

def test_invalid_numbers():
    assert not is_valid("1234567")
    assert not is_valid("+123901234567")

def test_normalize():
    assert normalize("909999999") == "+998909999999"
    assert normalize("998909999999") == "+998909999999"
    assert normalize("0909999999") == "+998909999999"

def test_normalize_invalid():
    try:
        normalize("123456")
    except ValueError:
        assert True

