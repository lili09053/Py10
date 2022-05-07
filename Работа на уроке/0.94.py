def my_decorator(func):
    def new_func(*args, **kwargs):
        result = func(*map(str.upper, args), **kwargs)
        return result

    return new_func()


print(*'asd 234 NTESwertyuihgc ghvSGG'.split())
print(my_decorator(*'asd 234 NTESwertyuihgc ghvSGG'.split()))



