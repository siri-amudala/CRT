'''input:[1,2,3,4,5]
output:[2,4,6,8,10] 4
li=list(map(int,input().split()))
res=[]
for i in li:
    res.append(i*2)
print(res)
print([i*2 for i in li])

#['a','b','c']=>"abc"
li1=['a','b','c']
res1=""
for ch in li1:
    res1+=ch
print(res1)
print("".join(li1))

Intermediante patterns:
1.pyramid
n=4
   *
  * *
 * * *
* * * *
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
    print(" "(n-1)+"* "*(n-1))

2. Inverted pyramid
n=4
output:
* * * *
 * * *
  * *
   *

n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
3.diamond
n = 4 
output:
       *
      * *
     * * *
    * * * *
     * * *
      * *
       *
n = int(input())
for i in range(1,n+1):
    print(" "*(n - i) + "* "*i)
for i in range(n-1,0,-1):
    print(" "*(n -i) + "* "*i)'''
    
'''4. 1
    1  2
   1  2  3
 1  2  3  4

n = int(input())
for i in range(1, n+1):
    print(" "*(n - i)+ " ".join([str(j) for j in range(1, i + 1)]))

for i in range(1, n+1):
    print(" "*(n - i)+" ".join([str(i) for j in range(1, i + 1)]))

   5.A
     B C
     D E F 
     G H I J'''

n = int(input())
ch=65
for i in range(n):
    for j in range(i+1):
        print(chr(ch),end=" ") 
        ch += 1
    print()

