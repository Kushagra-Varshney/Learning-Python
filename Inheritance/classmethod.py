class MyClass:
    val = 10
    @classmethod
    def show_val(cls):
        print(cls.val)

# Calling the class method
obj = MyClass()
obj.val = 20
obj.show_val() # This is a class method. hence it prints 10 ie class attribute
