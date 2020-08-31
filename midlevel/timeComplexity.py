def solution(X, Y, D):
   distance = Y - X
   if distance % D == 0:
      return distance//D
   else:
      return distance//D + 1


num=solution(10,85,30)
print(num)