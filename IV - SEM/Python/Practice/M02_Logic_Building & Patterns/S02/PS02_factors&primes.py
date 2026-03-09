''' 1 
input:12
output: 1 2 3 4 6 12 
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
print(n)
2
input: 12
output: 6 (factors count)
n=int(input())
count=0
for i in range(1,n//2+1):
    if n%i==0:
        count+=1
print(count +1)

3
check if a number is prime or not
n=int(input())
count=0
for i in range(2,n//2+1):
    if n%i==0:
        count+=1
print("Not Prime") if count>0 else print("Prime")

4
display all prime numbers in given range
start=int(input())
end=int(input())
if start==1:
    start=2
for num in range(start,end+1):
    count=0
    for i in range(2,num//2+1):
        if num%i==0:
            count+=1
            
    if count==0:
        print(num,end=' ')  
        
5
factorial of a number
input:5
output:120
---->0! = 1
---->1! = 1
---->-ve=no factorial
n=int(input())
if n<0:
    print("No factorial")
elif n==0 or n==1:
    print("Factorial:",1)
else:
    fact=1
    for i in range(2,n+1):
        fact*=i
    print(fact)

6
gcd of two numbers
input: 12 15
output: 3
a,b=map(int,input().split())
while b:
    a,b=b,a%b
print(a)

import math
print(math.gcd(a,b))

7
fibonacci series
input: 10
output: 0 1 1 2 3 5 8
'''
n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
print()
#using list
fib=[0,1]
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
for i in fib:
    print(i,end=' ')





            
