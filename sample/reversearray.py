from audioop import reverse


input1=input().split(" ")
reverse1=[]
i=len(input1)
while i > 0:
    reverse1 +=  input1[i-1]
    i=i-1

print(reverse1)

print(input1[::-1])