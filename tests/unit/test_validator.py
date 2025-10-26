from src.validator import validate_email

def test_email_valido():
    assert validate_email("eduarda@senac.com")

def test_email_sem_arroba():
    assert not validate_email("eduarda.senac.com")

def test_email_vazio():
    assert not validate_email("")
