class Singleton:
    __instanse = None

    def __new__(cls):
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)
        return cls.__instanse