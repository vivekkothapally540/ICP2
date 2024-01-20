heights_list = []
heights_in_cm = []
while True:
    inp_1 = input("Enter heights of customers(inches) (press q to quit):")
    if inp_1 == 'q':
        break
    else:
        heights_list.append(inp_1)

print("L1: ", heights_list)
heights_in_cm = [int(height) * 2.54 for height in heights_list]
print("Output: ", heights_in_cm)