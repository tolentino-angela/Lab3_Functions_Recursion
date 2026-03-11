from access_control import compute_access_level, validate_access, audit_log


CONTROL_NUM = 0


@audit_log
def run_auth():
    level = compute_access_level(CONTROL_NUM)
    decision = validate_access(level, CONTROL_NUM)

    print("Access Level:", level)
    print("Decision:", decision)


run_auth()
CONTROL_NUM = 0
FAVORITE_ARTIST = "SEVENTEEN"


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper


@log_decorator
def signal_shutdown(power, calls=0):

    print("Signal strength:", power)

    if power == 0:
        return calls

    return signal_shutdown(power - 1, calls + 1)


power = CONTROL_NUM + len(FAVORITE_ARTIST)

total = signal_shutdown(power)

print("Total calls:", total)
from media_engine import play_count_stream, monitor


CONTROL_NUM = 0
FAVORITE_ARTIST = "SEVENTEEN"

limit = CONTROL_NUM + len(FAVORITE_ARTIST)


@monitor
def run_stream():

    total = 0
    count = 0

    for x in play_count_stream(limit):
        print("Play:", x)
        total += x
        count += 1

    print("Total plays:", total)
    print("Records:", count)


run_stream()