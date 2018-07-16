def decorator(fn):
    def wrapper(*args, **kwargs):
        print('******')
        print(fn(*args, **kwargs))
        print('******')
    return wrapper


def table(subbol):
    def decorator_table(fn):
        def wrapper(*args, **kwargs):
            a = fn(*args, **kwargs)
            print(subbol * (len(a) + 4))
            print(subbol, a.upper(), subbol)
            print(subbol * (len(a) + 4))
        return wrapper
    return decorator_table


# @table('#')
# def print_name(name):
#     return name


@table('#')
def read_name():
    return input('name: ')

# print_name('hhhh')
read_name()
