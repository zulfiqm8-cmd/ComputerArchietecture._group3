
# GROUP 3 - QUESTION 2
# 8-bit Rotate Operations (ROR and RCR)

def rotate_right(value):
    return (value >> 1) | ((value & 1) << 7)


# (a) Rotate Right without Carry (ROR)

print("(a) ROTATE RIGHT WITHOUT CARRY (ROR)")

number = int('11010101', 2)

print("Original Number:", format(number, '08b'))

for i in range(2):
    number = rotate_right(number)
    print("After rotation", i + 1, ":", format(number, '08b'))

print("Final Result:", format(number, '08b'))


# (b) Rotate Right with Carry (RCR)

print("\n(b) ROTATE RIGHT WITH CARRY (RCR)")

number = int('11010101', 2)
carry = 0

print("Original Number:", format(number, '08b'))
print("Initial Carry:", carry)

for i in range(2):
    new_carry = number & 1
    number = (number >> 1) | (carry << 7)
    carry = new_carry

    print("After rotation", i + 1, ":", format(number, '08b'))
    print("Carry:", carry)

print("Final Result:", format(number, '08b'))
print("Final Carry:", carry)
