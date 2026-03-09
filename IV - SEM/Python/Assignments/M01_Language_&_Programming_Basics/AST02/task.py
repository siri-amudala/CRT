def even_odd(n: int) -> str:
   if n%2!=0:
       return "Weird"
   else:
       if n>=2 and n<=5:
           return "Not Weird"
       elif n>=6 and n<=20:
           return "Weird"
       elif n>=20:
           return "Not Weird"
   


if __name__ == '_main_':
    n = int(input())
    print(even_odd(n))