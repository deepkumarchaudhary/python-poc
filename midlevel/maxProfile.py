import sys

def solution(A):
    min_price = sys.maxsize
    #print(min_price)
    max_profit = 0
    for a in A:
        min_price = min([min_price, a])
        #print(a,min_price)
        max_profit = max([max_profit, a - min_price])
        #print(max_profit)
    return max_profit




A=[23171,21011,21123,21366,21013,21367]
print("Max profile is:", solution(A))
