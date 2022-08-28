# python script to print all Prime numbers under 100

for i in range(2,100):
    for b in range(2,i):
        c=i%b
        if c==0:
            break
    else:
        print(i,end=' ')
    
"""   
    for b in range(2,i+1):
        # c=i%b
        # count =1
        if (i%b)==0:
            # count+=1
            # if count>1:
                 break
        print(i,end=' ') """
