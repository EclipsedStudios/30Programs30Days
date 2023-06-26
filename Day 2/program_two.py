import os

#Asks for location of the folder and renames all the files in that folder with the given name and a number

def renamer(name):
    folder = input("Enter the folder name: ")
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{folder}\{name}_{str(count)}.jpg"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder         
        os.rename(src, dst)

name = input("Enter the intended filename: ")
renamer(name)