file = open(r"C:\Users\rhorn\OneDrive\Pulpit\1\liczby.txt", "r")
binaryNumbers = file.readlines()
for i in range(len(binaryNumbers) - 1):
    binaryNumbers.insert(i, binaryNumbers[i].strip())
    binaryNumbers.pop(i + 1)
divByTwoCounter = 0
divByEightCounter = 0
counter = 0
lineCounter = 0
shortestNumber = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
                 "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111" \
                 "11111111111111111111111111111111111111111111111111"
longestNumber = "0"
longestIndex = 0
shortestIndex = 0

for line in binaryNumbers:
    numberCounter = 0
    boolean = True
    lineCounter += 1

    for char in line:
        if char == "0":
            numberCounter += 1
        else:
            numberCounter -= 1

    if line[len(line) - 1] == "0":
        divByTwoCounter += 1

    for i in range(1, 4):
        if line[len(line) - i] == "1":
            boolean = False
            break

    if len(line) >= len(longestNumber):
        if len(line) == len(longestNumber):
            for i in range(1, len(line)):
                if line[i] > longestNumber[i]:
                    longestNumber = line
                    longestIndex = lineCounter
                elif line[i] < longestNumber[i]:
                    break

        else:
            longestNumber = line
            longestIndex = lineCounter

    if len(line) <= len(shortestNumber):
        if len(line) == len(shortestNumber):
            for i in range(1, len(line)):
                if line[i] < shortestNumber[i]:
                    shortestNumber = line
                    shortestIndex = lineCounter
                elif line[i] > shortestNumber[i]:
                    break

        else:
            shortestNumber = line
            shortestIndex = lineCounter
    if boolean:
        divByEightCounter += 1

    if numberCounter > 0:
        counter += 1

print(counter)
print(divByTwoCounter)
print(divByEightCounter)
print(longestIndex)
print(shortestIndex)