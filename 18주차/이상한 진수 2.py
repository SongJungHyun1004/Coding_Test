binary = input()
idx = binary.find('0')
binary = list(binary)
if idx == -1:
    binary[-1] = '0'
else:
    binary[idx] = '1'
binary = ''.join(binary)
print(int(binary, 2))