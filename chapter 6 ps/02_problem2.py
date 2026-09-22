s1 = int(input("marks in subject 1 out of 100: "))
s2 = int(input("marks in subject 2 out of 100: "))
s3 = int(input("marks in subject 3 out of 100: "))

if(s1>33 and s2>33 and s3>33 and ((s1+s2+s3)/3)>=40):
    print("passed")

else:
    print("failed")

