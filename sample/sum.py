string = input("Enter a String : ") 
result=''
for i in string:  
#iterating through each character of the string
    if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):  
     #seaching for vowels
        i = ''  
#if vowel found replace it with empty string
    result += i 
    #concatenate rest of the string
print("String after removing the vowels :",result)