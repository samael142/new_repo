class DivByZero(Exception):

    def __init__(self):
        self.txt = "division by zero is not allowed"

    def __str__(self):
        return self.txt


def div(dividend, divisor):
    try:
        if divisor != 0:
            return f"{dividend} / {divisor} = {dividend / divisor}"
        else:
            raise DivByZero
    except DivByZero as err:
        return err


a = div(15, 0)
print(a)
