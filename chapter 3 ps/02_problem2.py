letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|> '''

Name = input("write your name ")
date = input("write the date ")


print(letter.replace("<|Name|>" , Name).replace("<|Date|>" , date))


