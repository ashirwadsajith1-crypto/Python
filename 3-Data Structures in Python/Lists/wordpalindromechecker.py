def wordspalindrome(words):
    str=0
    emptylist=[]
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            str+=1
            emptylist.append(i)
    print(emptylist)
    return str
a=wordspalindrome(['123', 'racecar', 'sos'])
print(a)



            
