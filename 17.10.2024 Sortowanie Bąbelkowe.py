file = open(r"D:\pythonProject\Text_Files\liczby.txt", "r")
numbers = []

def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

for i in file:
    temp = ""
    for j in i:
        if j != " " and j != "\n":
            temp += j
        else:
            temp = int(temp)
            numbers.append(temp)
            temp = ""
    if temp != "":
        temp = int(temp)
        numbers.append(temp)

numbers = remove_items(numbers,"")
temp = 0

for i in range(len(numbers)):
    for j in range(1,len(numbers)-i):
        if numbers[j-1] > numbers[j]:
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]

for i in numbers:
    print(i)