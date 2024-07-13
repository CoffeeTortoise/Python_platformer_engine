

class Number:
    """A secure class for storing int or float. Supports all basic arithmetic and
    logical operation with its own type. Has property: num. Not recommended to use
    it for numbers over 10_000(int type)."""
    def __init__(self, num: int | float = 0):
        self.__msg = 'This is not a number!'
        self.__warn = 'This is not a Number object!'
        self.__div = 'You can\'t divide by zero!'
        if (type(num) is int) or (type(num) is float):
            self.__num = num
        else:
            raise TypeError(self.__msg)

    @property
    def num(self):
        """Value of a number"""
        return self.__num

    @num.setter
    def num(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            del self.__num
            self.__num = new
        else:
            raise TypeError(self.__msg)

    def __repr__(self):
        return f'{self.__num}'

    def __eq__(self, other):
        if type(other) is type(self):
            if other.num == self.__num:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if type(other) is type(self):
            if other.num == self.__num:
                return False
            else:
                return True
        else:
            return True

    def __lt__(self, other):
        if type(other) is type(self):
            return self.__num < other.num
        else:
            return False

    def __gt__(self, other):
        if type(other) is type(self):
            return self.__num > other.num
        else:
            return True

    def __le__(self, other):
        if type(other) is type(self):
            return self.__num <= other.num
        else:
            return False

    def __ge__(self, other):
        if type(other) is type(self):
            return self.__num >= other.num
        else:
            return True

    def __add__(self, other):
        if type(other) is type(self):
            res: int | float = self.__num + other.num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __radd__(self, other):
        if type(other) is type(self):
            res: int | float = other.num + self.__num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __iadd__(self, other):
        if type(other) is type(self):
            self.__num += other.num
            return self
        else:
            raise TypeError(self.__warn)

    def __sub__(self, other):
        if type(other) is type(self):
            res: int | float = self.__num - other.num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __rsub__(self, other):
        if type(other) is type(self):
            res: int | float = other.num - self.__num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __isub__(self, other):
        if type(other) is type(self):
            self.__num -= other.num
            return self
        else:
            raise TypeError(self.__warn)

    def __mul__(self, other):
        if type(other) is type(self):
            res: int | float = self.__num * other.num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __rmul__(self, other):
        if type(other) is type(self):
            res: int | float = other.num * self.__num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __imul__(self, other):
        if type(other) is type(self):
            self.__num *= other.num
            return self
        else:
            raise TypeError(self.__warn)

    def __truediv__(self, other):
        if type(other) is type(self):
            if other.num != 0:
                res: int | float = self.__num / other.num
                return Number(res)
            else:
                raise ZeroDivisionError(self.__div)
        else:
            raise TypeError(self.__warn)

    def __rtruediv__(self, other):
        if type(other) is type(self):
            if self.__num != 0:
                res: int | float = other.num / self.__num
                return Number(res)
            else:
                raise ZeroDivisionError(self.__div)
        else:
            raise TypeError(self.__warn)

    def __itruediv__(self, other):
        if type(other) is type(self):
            if other.num != 0:
                self.__num /= other.num
                return self
            else:
                raise ZeroDivisionError(self.__div)
        else:
            raise TypeError(self.__warn)

    def __floordiv__(self, other):
        if type(other) is type(self):
            res: int | float = self.__num // other.num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __rfloordiv__(self, other):
        if type(other) is type(self):
            res: int | float = other.num // self.__num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __ifloordiv__(self, other):
        if type(other) is type(self):
            self.__num //= other.num
            return self
        else:
            raise TypeError(self.__warn)

    def __mod__(self, other):
        if type(other) is type(self):
            res: int | float = self.__num % other.num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __rmod__(self, other):
        if type(other) is type(self):
            res: int | float = other.num % self.__num
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __imod__(self, other):
        if type(other) is type(self):
            self.__num %= other.num
            return self
        else:
            raise TypeError(self.__warn)

    def __pow__(self, other):
        if type(other) is type(self):
            res: int | float = pow(self.__num, other.num)
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __rpow__(self, other):
        if type(other) is type(self):
            res: int | float = pow(other.num, self.__num)
            return Number(res)
        else:
            raise TypeError(self.__warn)

    def __ipow__(self, other):
        if type(other) is type(self):
            self.__num **= other.num
            return self
        else:
            raise TypeError(self.__warn)

    def __neg__(self):
        res: int | float = -self.__num
        return Number(res)

    def __vpos__(self):
        res: int | float = self.__num
        return Number(res)

    def __abs__(self):
        res: int | float = abs(self.__num)
        return Number(res)

    def __del__(self):
        print('Number has been deleted')
