__author__ = 'levor23 '

from string import ascii_lowercase, ascii_uppercase

def checkio(data):
    if len(data)>=10:
        alpha_lower=False
        alpha_upper=False
        char_digit=False
        for i in data:
            if i in ascii_uppercase:
                alpha_upper=True
            elif i in ascii_lowercase:
                alpha_lower=True
            elif i.isdigit():
                char_digit=True
            else:
                continue
        return alpha_upper and alpha_lower and char_digit
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"

