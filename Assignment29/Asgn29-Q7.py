"""Python script to count the number of Python keywords occurring in a python
source file"""

import keyword

# a = keyword.kwlist
# print(type(a),a)

def search(filename):
    list = keyword.kwlist
    try:
        f = open(filename,'r')
        line_count = 0
        for line in f.readlines():
            line_count+=1
            strlist=line.split(' ')
            word_count =0
            for w in strlist:
                w = w.replace('\n','')
                word_count+=1
                for s in list:
                    if s==w:
                        print(line_count,word_count,s)
                    else:
                        pass
        f.close()
    except FileNotFoundError:
        print("file not found")

search('cities.txt')