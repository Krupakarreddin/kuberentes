from math import floor


num=int(input("enter a number"))
sum=0
temp=num
while num>0:
    rem=num % 10
    sum=sum + (rem*rem*rem)
    num=floor(num / 10)

if sum==temp:
    print("armstrong") 

string="krupa"
revarray=[]
index=len(string)
while index > 0:
    revarray += string[index-1]
    index = index-1


print("".join(revarray))


