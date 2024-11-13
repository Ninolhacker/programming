# fin = open('lists.txt')
# line=fin.readline()#legge la n riga fin.readline(3)
# word=line.strip('a')#replace a certain character
# print(word)

dictionary={}
fin = open('lists.txt')
line=fin.readline()

for line in fin:
    word=line.strip()
    charw=len(word)
    if charw not in dictionary: 
        dictionary[charw]= [word]
    else:
        dictionary[charw].append(word)
for chiave, valore in dictionary.items():
    print(f"{chiave}: {valore}")