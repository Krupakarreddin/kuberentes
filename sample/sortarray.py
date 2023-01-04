inputt=list(map(int,input().split(" ")))

for i in range(len(inputt)):
    for j in range(len(inputt)-1):
        if inputt[i] < inputt[j]:
            temp = inputt[i]
            inputt[i] = inputt[j]
            inputt[j] =  temp

print(inputt)
