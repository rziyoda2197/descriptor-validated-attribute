class PositiveNumberDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{self.name} attribute must be a positive number")
        instance.__dict__[self.name] = value

class MyClass:
    x = PositiveNumberDescriptor()

obj = MyClass()
obj.x = 10  # ishlashi mumkin
obj.x = -5  # ishlamaydi
obj.x = 3.14  # ishlashi mumkin
obj.x = "hello"  # ishlamaydi
