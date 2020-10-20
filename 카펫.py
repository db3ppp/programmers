완전탐색_level2

import math

def solution(brown, yellow):
    x = ( (4+brown) + math.sqrt((4+brown)**2 - 16*(brown+yellow)) )/4
    y = (brown + yellow) / x
    return [x,y]

#brown + yellow = x * y
#yellow = (x-2) * (y-2)
#근의공식
