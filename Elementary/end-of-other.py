__author__ = 'levor23'


def checkio(words_set):
    for word1 in words_set:
        for word2 in words_set:
            if word1 == word2:
                continue
            else:
                if word1.endswith(word2):
                    return True
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"