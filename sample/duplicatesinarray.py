list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(type(list1))
repeated=[]

for i in range(len(list1)):
    j=i+1
    for j in range(j,len(list1)):
        if list1[i]== list1[j] and list[i] not in repeated:
            repeated.append(list1[i])

print(repeated)
