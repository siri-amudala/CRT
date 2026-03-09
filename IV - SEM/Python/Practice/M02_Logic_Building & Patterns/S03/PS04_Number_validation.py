''' Arm strong number:
input: 153
output: Armstrong number

input: 24
output: Not an Armstrong number'''

n=int(input("Enter a number: "))
count =len(str(n))
s=0
for digit in str(n):
    s+=int(digit)**count

print("Armstrong number" if s==n else "Not an Armstrong number")

'''perfect number:
input: 6
output: Perfect number
6===1,2,3
1+2+3=6'''

n=int(input("Enter a number: "))
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
print("Perfect number" if s==n else"not a perfect number")

'''Strong number:
input: 123
output: not a strong number

explanation: 1! + 2!+ 3!= 1+2+6=9'''
def factorial(n):
    if n<0:
        return "no factorial for -ve"
    elif n==0 or n==1:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f*=i
        return f
    
n=int(input("Enter a number: "))
s=0 
for digit in str(n):
    s+=factorial(int(digit))
print("Strong number" if s==n else "Not a strong number")