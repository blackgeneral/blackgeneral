# Speaking in Tongues about google code jam problem in 2012

def solvelist(ilist, olist, sdict):    #change password_dict used by example
    for i in range(len(ilist)):
        sdict[ilist[i]] = olist[i]

    return sdict            


def solvepwd(Is1, Is2, Is3, Os1, Os2, Os3):
    inputList1 = list(Is1)
    inputList2 = list(Is2)
    inputList3 = list(Is3)
    outputlist1 = list(Os1)
    outputlist2 = list(Os2)
    outputlist3 = list(Os3)
    solveDict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0, ' ':' '}

    solveDict = solvelist(inputList1, outputlist1, solveDict)
    solveDict = solvelist(inputList2, outputlist2, solveDict)
    solveDict = solvelist(inputList3, outputlist3, solveDict)

    return solveDict

def firstDict(pwdict):
    pwdict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0, ' ':' '}

    pwdict['a'] = 'y'
    pwdict['o'] = 'e'
    pwdict['z'] = 'q'

    inputString1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
    inputString2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
    inputString3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

    outputString1 = 'our language is impossible to understand'
    outputString2 = 'there are twenty six factorial possibilities'
    outputString3 = 'so it is okay if you want to just give up'

    pwdict1 = solvepwd(inputString1, inputString2, inputString3, outputString1, outputString2, outputString3)

    return pwdict1

    """
    Dict setting fuction

    """

# Main Function #

OriginDict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

OriginDict1 = firstDict(OriginDict)
answerlist = []

testcase = int(input())
for i in range(testcase):
    Istring = list(input())
    str1=''
    for j in range(len(Istring)):
        str1 = str1 + OriginDict1[Istring[j]]

    print("case # %d : %s" %(i+1, str1))
