n = int(input("Enter the size: "))

print("Pattern 1:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print("Floyd's Triangle:")
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("Diamond:")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()