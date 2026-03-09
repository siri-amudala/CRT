def count_digits(n: int) -> int:
    count = 0 
    while n>0:
        count+=1
        n = n//10
    return count

if __name__ == "_main_":
    n = int(input())
    print(count_digits(n))