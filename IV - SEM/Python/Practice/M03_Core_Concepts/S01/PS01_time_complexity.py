li=[10,20,30,40,50]
print(li[2])

li.append(60)

li.insert(0,100)
print(li)


n=int(input())
for i in range(n):
    for j in range(n):
        print(i,j,end=" ")

def  Linear_search(li,target):
    for i in range(len(li)):
        if li[i] == target:
            return 1
    return  -1


Linear_search([12,45,78,69,32,46],12)   
linear_search([12,45,78,69,32,46],78)
linear_search([12,45,78,69,32,46],46)
linear_search([12,45,78,69,32,46],100)