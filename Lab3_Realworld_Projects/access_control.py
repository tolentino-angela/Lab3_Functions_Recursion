# access_control.py

FAVORITE_ARTIST = "SEVENTEEN"   


def compute_access_level(control):
    access_level = control * 3 + len(FAVORITE_ARTIST)
    return access_level


def validate_access(level, control):
    threshold = control * 5

    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"


def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper
