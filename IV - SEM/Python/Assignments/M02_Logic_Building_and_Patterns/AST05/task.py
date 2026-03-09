def number_triangle(n: int) -> str:
    s=""
    for i in range(1,n+1):
        s+="".join([str(j) for j in range(1,i+1)])+"\n"
    return s.rstrip()

if __name__ == "_main_":
    n = int(input())
    print(number_triangle(n))