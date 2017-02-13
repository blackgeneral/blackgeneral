# Fair and Square Solve

testcase = int(input())  # case number

for i in range(testcase): # first for phrase about Test_Case
    STRLIST = []  # list about integer
    input_list = str(raw_input()) # transfer integer to String
    input_list = input_list.split() # split to one-bit in List

    for a in range(len(input_list)): # List transfer to Integer List
        STRLIST.append(int(input_list[a]))

    #print(STRLIST)
    #print("AAAA")
    startNum = STRLIST[0] # Start number
    endNum = STRLIST[1] # End number
    count = 0 # Count number

    for j in range(startNum,endNum+1): # Second for phrase about Case-by-Case
        startstr = j
        compstr = str(j)

        FFlist = []
        Slist = []
        Flist = []
        FFlist = list(compstr.split()) # FFlist was filled by String List that one-bit
        
        for tt in range(len(FFlist[0])): # FFlist transfer to Flist
            Flist.append(FFlist[0][tt])    
        for aa in Flist:
            Slist.append(aa)
        Slist.reverse()
        if Flist == Slist: 
            startstr = 0
            F_list = []
            S_list = []
            startsqure = j**0.5
            if startsqure % 1 == 0: # if result is integer
                startsqure = int(j**0.5) #transfer to integer
                squrestr = str(startsqure)
                ARR_list = list(squrestr.split()) #ARR_list was filled by String List that one-bit

                for b in range(len(ARR_list[0])):
                    F_list.append(ARR_list[0][b]) # F_list was filled by ARR_list[0]'s ransge

                for bb in F_list:
                    S_list.append(bb)
                S_list.reverse()
                #print(F_list, S_list)
                if cmp(F_list, S_list)==0:
                #    print(Flist, Slist)
                    count += 1
       
    print "case # %d : %d" %(i+1, count)
