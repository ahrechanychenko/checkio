__author__ = 'levor23'

def checkio(number):
    return reduce(lambda res, x: res * x, (int(x) for x in str(number).replace("0", "")) , 1)

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

