#How to reverse a number
num = int(input("Enter the number : "))
rev_num = 0
while(num>0):
    #logic
    rem = num%10
    rev_num= (rev_num*10)+rem
    num = num//10
print("Result : ",rev_num)
