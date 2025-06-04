def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) * 2, end="")
        print("* " * (2 *i - 1))
T = int(input().strip())
for i in range(T):
    n = int(input("ENTER A NUMBER "))
    pyramid(n)