x=input("Enter The FileName: ")
print(type(x))
i=0
j=0
count=1
e={}
while(x[i]!='.'):
    i+=1
while((i+1)<len(x)):
    e[j]=x[i+1]
    i+=1
    j+=1
ext=e[0]
while(count<j):
    ext+=e[count]
    count+=1
if(ext=='py'):
    print("This Is A Python File!")
elif(ext=='c'):
    print("This Is A C File!")
elif(ext=='cpp'):
    print("This Is A C++ File!")
elif(ext=='txt'):
    print("This Is A Text File!")
elif(ext=='pdf'):
    print("This Is A PDF File!")
elif(ext=='jpeg'):
    print("This Is A JPEG image File!")
elif(ext=='xls'):
    print("This Is An Excel File!")
#Any Other File Name Other Than The Above Mentioned Can't Be Idenified By This Program
#This Is a Limitation Of This Code
else:
    print("!!Filename Not Recognized!!")
