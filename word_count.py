

def word_count(mytext):
    alphabet= "".join([chr(i) for i in range(ord('a'),ord('a')+26)])
    lowertext=mytext.lower()
    mydictionary=dict()
    newstr=str()
    for i in lowertext:
        if i not in alphabet:
            newstr += " "
        if i in alphabet:
            newstr += i
    z=newstr.split()
    for i in z:
       mycount=z.count(i)
       mydictionary[i]=mycount
    return(mydictionary)

def analyze(count_dictionary):
    element0list=list()
    for i in count_dictionary:
        if len(i)>1:
            element0list.append(count_dictionary[i])
    element0=sum(element0list)
    valuelist=list()
    for i in count_dictionary:
        valuelist.append(count_dictionary[i])
    maxvalue=max(valuelist)
    element1=set()
    for i in count_dictionary:
        if count_dictionary[i]==maxvalue:
            element1.add(i)
    lengthlist=list()
    for i in count_dictionary:
        length=len(i)
        lengthlist.append(length)
    maxlength=max(lengthlist)
    element2=set()
    for i in count_dictionary:
        if len(i)==maxlength:
            element2.add(i)
    answerlist=[element0, element1, element2]
    return(answerlist)
    
def top_words(count_dictionary,n):   
    frequencylist=list()
    othercrazylist=list()
    for i in count_dictionary:
        frequencylist.append(count_dictionary[i]) 
    while len(othercrazylist)<n:
        maxfrequency=max(frequencylist)
        othercrazylist.append(maxfrequency)
        for i in frequencylist:
            if i==maxfrequency:
                frequencylist.remove(i)
                frequencylist.append(0)
    else:       
        crazylist=list()
        for i in count_dictionary:
            if count_dictionary[i] in othercrazylist:
                crazytuple=(i,count_dictionary[i])
                crazylist.append(crazytuple)
        for i in crazylist:
            crazylist.sort(key=lambda tup: tup[1], reverse=True)
    return(crazylist)