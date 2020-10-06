
#Numbers = input('Enter numbers: ')
Numbers = [2, 6, 25, 17, 1]
xor = 0
for num1 in Numbers:
    i = Numbers.index(num1)+1
    for num2 in Numbers[i:]:
        xor1 = num1 ^ num2
        if xor1 > xor:
            xor = xor1
print ('Output:', xor)
