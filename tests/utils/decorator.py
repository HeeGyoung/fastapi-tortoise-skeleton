import functools

from tortoise import connections
from tortoise.contrib.test import TransactionTestContext


def use_db(argument):
    def function_decorator(function):
        @functools.wraps(function)
        async def wrapper(*args, **kwargs):
            _db = connections.get(argument)
            async with TransactionTestContext(_db._in_transaction().connection):
                result = await function(*args, **kwargs)
            return result

        return wrapper

    return function_decorator


def set_db(argument):
    def class_decorator(cls):
        for key in dir(cls):
            value = getattr(cls, key)
            if key.startswith("test_"):
                decorator = use_db(argument)
                setattr(cls, key, decorator(value))
        return cls

    return class_decorator
