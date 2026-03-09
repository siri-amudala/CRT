def reverse_number(n: int) -> int:
    n = str(n)
    return int(n[::-1])

if __name__ == "_main_":
    n = int(input())
    print(reverse_number(n))