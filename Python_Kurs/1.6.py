from idlelib.configdialog import is_int
from os.path import isabs
from sre_compile import isstring
from xml.etree.ElementTree import tostring


def niepodzielneprzeztrzyipodowjoneparzyste(listwhole):
    notdivby3list = [i if i%2 == 0 else i*2 for i in listwhole if i%3 != 0]
    return notdivby3list


print(is_int("4a"))
listawhole = [i for i in range(101)]
print([i for i in niepodzielneprzeztrzyipodowjoneparzyste(listawhole)])