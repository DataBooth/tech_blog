from pathlib import Path
from functools import wraps

def arg_from_file(content_arg="content", encoding="utf-8"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            content = kwargs.get(content_arg)
            if content and Path(content).is_file():
                with open(content, 'r', encoding=encoding) as file:
                    kwargs[content_arg] = file.read()
            return func(*args, **kwargs)
        return wrapper
    return decorator