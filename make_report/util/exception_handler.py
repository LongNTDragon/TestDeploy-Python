import functools
import traceback


def exception_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            error_msg = traceback.format_exc()
            print(f"\n{error_msg}\n")
    return wrapper
