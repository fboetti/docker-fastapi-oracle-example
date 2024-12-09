__all__ = [
    "Singleton",
]


class Singleton(type):
    """
    Define a Singleton class that lets clients access its unique instance.
    """
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
