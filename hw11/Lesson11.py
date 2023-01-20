import datetime
import inspect

func_name = None

def my_decorator_func(func):
    def deco_func(*args, **kwargs):
        global func_name
        frame = inspect.currentframe()
        func_name = inspect.getframeinfo(frame).function
        res = func(*args, **kwargs)
        now_ = datetime.datetime.now()
        print(f'The function name is {func_name} - was called at {now_.strftime("%H:%M")}\n')
        return res
    return deco_func


@my_decorator_func
def my_func():
    print('This is my func')


my_func()


class ContextManager:
    def __init__(self):
        print('=' * 10)
        print('What is the sense of this task?')

    def __enter__(self):
        # print('='*10)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(exc_value)
            return True
        print('=' * 10)


with ContextManager() as manager:
    print('This is the test Context manager without sense')

print('\n')
try:
    print('='*10)
    print('What is the sense of this task?')
except Exception as e:
    print('Some exception: {e}')
else:
    print('This is the test Context manager without sense with try except')
finally:
    print('='*10)

# CustomExeption


class MyCustomException(Exception):
    def __init__(self):
        message = 'Custom exception is occurred!'
        super().__init__(message)


raise MyCustomException()

