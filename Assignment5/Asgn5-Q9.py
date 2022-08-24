# python script to use NOT IN operator to display the data not present in list
a = "hello, prime, iNeuron"
b = "iNeuron"
if b not in a:
    print(f"{b} is not in a")
else:
    print(f"{b} is in a")