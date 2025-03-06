from idlelib.configdialog import is_int
from os.path import isabs
from sre_compile import isstring
from xml.etree.ElementTree import tostring

#Nie podzielne przez 3 i podwojone parzyste
def NP3X2(listwhole):
    notdivby3list = [i if i%2 == 0 else i*2 for i in listwhole if i%3 != 0]
    return notdivby3list


print(is_int("4a"))
listawhole = [i for i in range(101)]
listaxd = [10,9,8,7,6]
print([i for i in NP3X2(listawhole)])
listadx = listaxd.index()
print(listaxd)