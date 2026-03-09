from typing import List


def Collatz_Sequence(n: int)-> List:
   seq = [n]
    
   while n != 1:
      if n % 2 == 0:
         n = n // 2
      else:
         n = 3 * n + 1
      seq.append(n)
    
   return seq

   pass
if __name__ == '_main_':
    n = int(input())
    print(Collatz_Sequence(n))