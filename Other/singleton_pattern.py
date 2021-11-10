class Singleton:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance


if __name__ == "__main__":
    inst1 = Singleton()
    inst2 = Singleton()

    print(id(inst1) == id(inst2))