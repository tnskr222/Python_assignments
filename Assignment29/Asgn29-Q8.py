# Python script to create a copy of a file

import os

d = r'C:\Users\tnskr\OneDrive\Desktop'

import shutil

print("Before copy of file")
print(os.listdir(d))

src = r'C:\Users\tnskr\OneDrive\Desktop\Resume\resume.pdf'
dest = r'C:\Users\tnskr\OneDrive\Desktop\resume1.pdf'

path = shutil.copyfile(src,dest)
print("after copy file")
print(os.listdir(d))
print('path of duplicate path')
print(path)