def linear(number, order):
    for a in range(1, len(number)):
        b = number[a]
        c = a - 1
        while c >= 0 and (number[c] > b if order == "ascending" else number[c] < b):
            number[c + 1] = number[c]
            c -= 1
            number[c + 1] = b
            print(number)

print("Linear Insertion Sort\n")
number1 = int(input("Input Number to be Sorted: "))

number = []
for i in range(number1):
    number2 = int(input("Input the Number: "))
    number.append(number2)

order = input("\"ascending or descending\": ")
print("\nResult: ", number)
