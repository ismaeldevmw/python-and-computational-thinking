# ejemplos rangos
print('EJEMPLOS RANGOS')
range1 = range(0, 7, 2)
for i in range1:
    print(i)

range2 = range(0, 8, 2)
for i in range2:
    print(i)

print(range1 == range2)
print(range1 is range2)

# calcular números impares
print('NÚMEROS IMPARES')
my_range =  range(0, 100)
result1 = []

for i in my_range:
    if i % 2 > 0:
        result1.append(i)

result2 = []
my_other_range =  range(1, 101, 2)

for i in my_other_range:
    result2.append(i)

print(result1[::])
print(result2[::])
print(result1 == result2)
print(result1 is result2)
