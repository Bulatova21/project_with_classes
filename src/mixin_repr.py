class MixinRepr:
    def __init__(self):
        print(self.__repr__())

    def __repr__(self):
        class_name = self.__class__.__name__
        data = []
        for name, value in self.__dict__.items():
            data.append(f"{name}={repr(value)}")
        return f"{class_name}({". ".join(data)})"

