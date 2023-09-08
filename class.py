class MyClass:
    def __init__(self, value):
        #for private data members we use underscore
        self._value = value

    #@property is use to make Getter method
    @property
    def value(self):
        return self._value

    # Setter method using @property decorator
    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value

    # Class method using @classmethod decorator
    # Class method must take cls
    @classmethod
    def create_instance(cls):
        return cls(5)

    # Static method using @staticmethod decorator
    # Static method may or maynot take parameters
    @staticmethod
    def static_method_example():
        print("This is a static method")

    # Custom data type class
    class CustomDataType:
        def __init__(self, data):
            self.data = data

    # Dunder methods
    def __str__(self):
        return "MyClass instance with value: " + str(self._value)
        # return f"MyClass instance with value: {self._value}"

    def __repr__(self):
        return "MyClass " + str(self._value)


# That will create an instance or object of MyClass
obj = MyClass(42)
# Accessing the getter
print(obj.value)  
# Accessing the setter
obj.value = 100  
print(obj.value)

new_obj = MyClass.create_instance()
print(new_obj.value)

obj.static_method_example()

custom_data = obj.CustomDataType("Custom Data")
print(custom_data.data)

#Dunder method str is called
print(str(obj))  # __str__ method
#Dunder method repr is called
print(repr(obj))  
