import re
def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    return re.match(pattern, email) is not None
