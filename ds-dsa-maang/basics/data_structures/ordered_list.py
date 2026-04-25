from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 1
od['c'] = 1
od['d'] = 1

print(od)

od.move_to_end('b')

capacity = 4

print(od)

od['e'] = 5

print(od)

#evit
if len(od) > capacity:
    od.popitem(last=False)

print(od)