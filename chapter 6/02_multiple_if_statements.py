a = int(input("Enter your age: "))

if(a%2 == 0):
    print("a is even")
if(a>=18):
    
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 as an age")

else:
    print("You are below the age of consent")


print("End of program")

