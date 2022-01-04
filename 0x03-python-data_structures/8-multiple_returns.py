#!/usr/bin/python3
def multiple_returns(sentence):
    lens = len(sentence)
    if(len(sentence) == 0):
        return(0, None)
    firstc = sentence[0]
    result = lens, firstc
    return(result)
