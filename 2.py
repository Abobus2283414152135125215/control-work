f=open('mat_dv.txt','r')
names = []
maxcount = 0
winers ={'8':[maxcount, names],'9':[maxcount, names],'10':[maxcount, names],"11":[maxcount, names]}

max_alg = 0
max_alg_names = []
max_geom = 0
max_geom_names = []

for i in f:
    work = i.split()
    if work[2]=='8':
        if int(work[3])+int(work[4]) > int(winers[work[2]][0]):
            winers[work[2]][1].clear()
            winers[work[2]][0] = int(work[3])+int(work[4])
            winers[work[2]][1].append(work[0]+work[1])
        if work[3]+work[4] == winers[work[2]][0]:
            winers[work[2]][1].append(work[0]+work[1])
    if work[2]=='9':
        if int(work[3])+int(work[4]) > int(winers[work[2]][0]):
            winers[work[2]][1].clear()
            winers[work[2]][0] = int(work[3])+int(work[4])
            winers[work[2]][1].append(work[0]+work[1])
        if work[3]+work[4] == winers[work[2]][0]:
            winers[work[2]][1].append(work[0]+work[1])
    if work[2]=='10':
        if int(work[3])+int(work[4]) > int(winers[work[2]][0]):
            winers[work[2]][1].clear()
            winers[work[2]][0] = int(work[3])+int(work[4])
            winers[work[2]][1].append(work[0]+work[1])
        if work[3]+work[4] == winers[work[2]][0]:
            winers[work[2]][1].append(work[0]+work[1])

    if work[2]=='11':
        if int(work[3])+int(work[4]) > int(winers[work[2]][0]):
            winers[work[2]][1].clear()
            winers[work[2]][0] = int(work[3])+int(work[4])
            winers[work[2]][1].append(work[0]+work[1])
        if work[3]+work[4] == winers[work[2]][0]:
            winers[work[2]][1].append(work[0]+work[1])

    #2

    if int(work[3]) > max_alg:
        max_alg_names.clear()
        max_alg =  int(work[3])
        max_alg_names.append(work[0]+work[1]+work[2])
    if  int(work[3]) == max_alg:
        max_alg_names.append(work[0]+work[1]+work[2])

    if int(work[4]) > max_geom:
        max_geom_names.clear()
        max_geom =  int(work[3])
        max_geom_names.append(work[0]+work[1]+work[2])
    if  int(work[4]) == max_geom:
        max_geom_names.append(work[0]+work[1]+work[2])




print(winers)

print(max_alg)
print(max_alg_names)

print()

print(max_geom)
print(max_geom_names)












