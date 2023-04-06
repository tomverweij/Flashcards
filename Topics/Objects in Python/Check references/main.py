def check(obj1, obj2):
    print(True if id(obj1) == id(obj2) else False)