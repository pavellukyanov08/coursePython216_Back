def limit_calls(max_calls):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.count > max_calls:
                raise ValueError(f'Function {func.__name__} cannot be called more than {max_calls} times.')
            wrapper.count += 1
            return func(*args, **kwargs)
        wrapper.count = 0
        return wrapper
    return decorator


@limit_calls(1)
def call():
    print('Hello world')


call()
call()
call()

