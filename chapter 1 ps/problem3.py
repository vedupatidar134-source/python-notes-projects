import os

# specify the directpry you want to list 
diretory_path = '/home/ved/Desktop/anime'

# list all files and directories in the specified path
contents = os.listdir(diretory_path)

# print each file and directory name
for item in contents:
    print(item)