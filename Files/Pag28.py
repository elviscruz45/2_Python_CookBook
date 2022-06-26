from collections import defaultdict

d = defaultdict(list)
print(type(d))

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)