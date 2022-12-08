# Python script to search whether a particular city is there in the file ‘cities.txt’ or not

def search(filename,word):
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
                if word ==w:
                    print(line_count,word_count)
                else:
                    pass
        f.close()
    except FileNotFoundError:
        print("file not found")

search('cities.txt','kadapa')