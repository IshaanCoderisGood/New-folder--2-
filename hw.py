def rightmost(n):
    position = 1
    while n & 1 == 0:
        n = n >> 1
        position += 1
    return position if n != 0 else 0

number = int(input("Enter a number: "))
result = rightmost(number)
print(f"position of set bit is: : {result}" if result else "no set bits")
