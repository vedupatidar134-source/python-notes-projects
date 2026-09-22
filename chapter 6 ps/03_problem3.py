p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

text = input("Enter your comment: ")

if(p1 in text or p2 in text or p3 in text or p4 in text):
    print("this is a scam")

else:
    print("copy is ready for pasta")