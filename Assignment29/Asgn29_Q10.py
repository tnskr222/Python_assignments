"""Python script to extract book data from a bookfile using pickle. Also print
extracted book data"""
import pickle

h = open('file1','rb')
s = pickle.load(h)
for key in s:
    print(key,':',s[key])
h.close()