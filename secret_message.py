__author__ = 'levor23'


def find_message(text):
    return ''.join([x for x in text if x.isupper()])

if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert find_message(u"How are you? "
                        u"Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message(u"hello world!") == "", "Nothing"
    assert find_message(u"HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
