def author(name):
    def wrapper(func):
        func.author = name
        return func
    return wrapper


@author("Author")
def add2(num: int) -> int:
    return num + 2


print(add2.author)
