from validator import check_email, validate_file

def test_check_email():
    assert check_email("test@example.com") == True
    assert check_email("wrong-email") == False

def test_validate_file():
    result = validate_file("emails.txt")
    assert len(result) == 2  # wrong-email and hello@world
