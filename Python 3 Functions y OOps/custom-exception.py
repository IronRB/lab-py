class CustomError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise CustomError('Two inputs must be integers.')
   c = a**b
except CustomError as e:
    print(e)  

try:
    a = 14 / 7
except ZeroDivisionError:
    print('oops!!!')
else:
    print('First ELSE')
try:
    a = 14 / 0
except ZeroDivisionError:
    print('oops!!!')
else:
    print('Second ELSE')          