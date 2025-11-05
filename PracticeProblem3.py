size = input("Enter list size: ")
size = int(size)

i = 0
even = 0
odd = 0

while(i<size):
    num=input("Enter a number: ")
    num=int(num)
    
    if(num%2==0):
        even+=1
    else:
        odd+=1
        
    i+=1
    
print("Even numbers: ", even)
print("Odd numbers: ", odd)
