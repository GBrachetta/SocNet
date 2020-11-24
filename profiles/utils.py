import uuid


def get_random_code():
    """Provides a random string to append to slug when users with same name"""

    code = str(uuid.uuid4())[:8].replace("-", "").lower()
    return code
