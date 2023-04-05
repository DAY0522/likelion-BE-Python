# 4. 


def count(List):
    #print(List)
    a=[]
    for i in List:
        if 'e' in i:
            #print(i)
            continue
        else:
            a.append(i)
    tupa=tuple(a)
    print(tupa)




  
animals = ('lion', 'tiger', 'penguin', 'dog', 'cat')

list1=list(animals)
#print(list1)
count(list1)
#print(list1)

