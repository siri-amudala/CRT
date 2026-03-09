def right_triangle(n: int) -> str:
    res=""
    for i in range(n):
        for j in range(i+1):
            res+="*"
        res+="\n"
    return res.rstrip()

if __name__ == "_main_":
    n = int(input())
    print(right_triangle(n))