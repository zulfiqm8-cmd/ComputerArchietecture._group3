
def to_binary(n):
    return format(n & 255, '08b')


def add(a, b):
    result = a + b
    binary = to_binary(result)

    overflow = result < -128 or result > 127

    print("First Number :", a, "=", to_binary(a))
    print("Second Number:", b, "=", to_binary(b))
    print("Binary Sum   :", binary)
    print("Decimal Sum  :", result if not overflow else result - 256)
    print("Overflow     :", "Yes" if overflow else "No")
    print()


print("8-BIT SIGNED BINARY ARITHMETIC")

print("\n(a) +48 + (+23)")
add(48, 23)

print("(b) (-46) - (-29)")
add(-46, 29)
