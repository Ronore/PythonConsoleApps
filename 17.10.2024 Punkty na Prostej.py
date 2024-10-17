file = open(r"Text_Files/punkty.txt", "r")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def returnx(self):
        return self.x

    def returny(self):
        return self.y

    def returnboth(self):
        return self.x, self.y


def areonthesameline(pa,pb,pc):
    pbx, pax, pcy, pay = pb.returnx(), pa.returnx(), pc.returny(), pa.returny()
    leftside = (pbx - pax) * (pcy - pay)
    rightside = (pb.returny() - pa.returny()) * (pc.returnx() - pa.returnx())
    if leftside == rightside:
        return True
    else:
       return False

def point_initialization(txtFile):
    numbers = []
    temp = ""
    for j in txtFile.readline():
        if j != " " and j != "\n":
            temp += j
        else:
            temp = float(temp)
            numbers.append(temp)
            temp = ""
    if temp != "":
        temp = float(temp)
        numbers.append(temp)
    pointa = Point(numbers[0],numbers[1])
    pointb = Point(numbers[2], numbers[3])
    pointc = Point(numbers[4], numbers[5])
    return pointa,pointb,pointc

pointa,pointb,pointc = point_initialization(file)


if areonthesameline(pointa, pointb, pointc):
    print(f"Punkty: A:{pointa.returnboth()} B:{pointb.returnboth()} C:{pointc.returnboth()} są na tej samej lini")
else:
    print(f"Punkty: A:{pointa.returnboth()} B:{pointb.returnboth()} C:{pointc.returnboth()} nie są na tej samej lini")