def sum_of_digits(n: int) -> int:
    temp = n
    res = 0
    while n > 0:
        digit = n % 10
        res = res + digit
        n = n // 10
    return res

if __name__ == "_main_":
    n = int(input())
    print(sum_of_digits(n))