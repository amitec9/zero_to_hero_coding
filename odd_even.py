#Enter the number find even number and odd number 
num = int(input("Enter the number : "))
for x in range(0,num):
    if(x%2) == 0:
        print("Even Numbers : ",x)
    else:
        print("Odd Numbers : ",x)
