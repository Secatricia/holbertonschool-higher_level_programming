#!/usr/bin/python3
def multiple_returns(sentence):
    if(len(sentence) == 0):
        return None
    lens = len(sentence)
    firstc = sentence[0]
    result = lens, firstc
    return result
 