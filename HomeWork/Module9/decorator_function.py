# Task 1
# def limit_calls(max_calls):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if wrapper.count > max_calls:
#                 raise ValueError(f'Function {func.__name__} cannot be called more than {max_calls} times.')
#             wrapper.count += 1
#             return func(*args, **kwargs)
#         wrapper.count = 0
#         return wrapper
#     return decorator
#
#
# @limit_calls(1)
# def call():
#     print('Hello world')
#
#
# call()
# call()
# call()


# Task 2
def validate_args(*args_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, args_type[i]):
                    raise TypeError(f'Expected argument of type {args_type[i]}, but got {type(arg)}')
            for key, arg in kwargs.items():
                if key in args_type and not isinstance(args, args_type[key]):
                    raise TypeError(f'Expected argument {key} of type {args_type[key]}, but got {type(arg)}')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_args(str, int, list)
def my_func(author, num_books, famous_books):
    print(f"{author} is the author of more than {num_books} books. The most famous of which are {','.join(famous_books)}")


my_func('Leo Tolstoy', 100, ['War and peace', 'Anna Karenina', 'Childhood'])
my_func('Leo Tolstoy', '100', ['War and peace', 'Anna Karenina', 'Childhood'])
