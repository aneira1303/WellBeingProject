def validate_nonempty(value):
    if not value or not str(value).strip():
        raise ValueError("Value cannot be empty")
    return True
