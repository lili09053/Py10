"""
def check_password(func):
    def new_func(*args, **kwargs):
        if input("Введите пароль от функции:") == "Qwerty":
            return func(*args, **kwargs)
        else:
            print('Отказано в доступе')

    return new_func()

@check_password
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

"""
#  ____________________________________________________

def check_password(func):
    password = None


    def new_func(*args, **kwargs):
        nonlocal password
        if password is None:
            password = input("Введите пароль от функции:")
        if password == "Qwerty":
                return  func(*args, **kwargs)
        else:

            print('Отказано в доступе')

    return new_func()

@check_password
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
