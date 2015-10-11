__author__ = 'levor23'


OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == "conjunction":
        return 1 if x == y == 1 else 0
    elif operation == "disjunction":
        return 0 if x == y == 0 else 1
    elif operation == "implication":
        return boolean(not x, y, "disjunction")
    elif operation == "exclusive":
        return 1 if x != y  else 0
    elif operation == "equivalence":
        return 1 if x == y else 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 0, u"exclusive") == 0, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"