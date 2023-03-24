# Task 1
# def limit_calls(max_calls):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             nonlocal max_calls
#             if max_calls > 0:
#                 func(*args, **kwargs)
#                 max_calls -= 1
#             else:
#                 raise ValueError('Max call limit is reached')
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
# def validate_args(*types):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             all_args = list(args)
#             all_args.extend(list(kwargs.values()))
#             for arg, type_of in zip(all_args, types):
#                 if type_of != type(arg):
#                     raise TypeError(f'Expected {type_of}, got {type(arg)} instead in {arg}')
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @validate_args(str, int, list)
# def my_func(author, num_books, famous_books):
#     print(f"{author} is the author of more than {num_books} books. The most famous of which are {','.join(famous_books)}")
#
#
# my_func('Leo Tolstoy', 100, ['War and peace', 'Anna Karenina', 'Childhood'])
# my_func('Leo Tolstoy', '100', ['War and peace', 'Anna Karenina', 'Childhood'])
