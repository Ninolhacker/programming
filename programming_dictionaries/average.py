d = {'120012': \
{'Operating Systems': 29, 'Mathematics': 19, \
'Programming': 28, 'Databases': 24}, \
'120230': \
{'Mathematics': 19, 'Statistics': 30, \
'Programming': 27, 'Algorithms': 21}, \
'121320': \
{'Statistics': 30, 'Programming': 27, \
'Mathematics': 30, 'Databases': 25} } 

subjectDict = {}
for key in d:
    print(d[key])

    for subjectKey in d[key]:
        if subjectKey not in subjectDict:
            subjectDict[subjectKey] = [d[key][subjectKey]]
        else: 
            subjectDict[subjectKey].append(d[key][subjectKey])

for key,value in subjectDict.items():
    print(f"{key} {value}")


for i in subjectDict:
    print(i ,": ",sum(subjectDict[i])/len(subjectDict[i]))
