n = int(input())
num = int(input())
reminder = []
quotient = num // n
reminder.append(num%n)
while quotient != 0:
    reminder.append(quotient%n)
    quotient = quotient // n
reminder = reminder[::-1]
equivalent = ''
for i in reminder:
    if i > 9:
        a = i - 9
        a = 64 + a
        equivalent+=chr(a)
    else:
        equivalent+=str(i)
print(equivalent)
