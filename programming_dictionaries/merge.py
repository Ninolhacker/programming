d1 = {'red': 10, 'blue': 4, 'green': 6}
d2 = {'blue': 31, 'green': 3, 'yellow': 5}
dmerge={}

for key in d1:
    dmerge[key]=d1.get(key,0)+d2.get(key,0)


print(dmerge)


