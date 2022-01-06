#print the fibonaccie series
first = 0  
sec = 1
nextt = first + sec
num = int(input("Enter the number : "))
print("Fibonaccie series : ",first,sec)
for i in range(3,num):
    print(nextt)
    first = sec
    sec = nextt
    nextt = first+sec
