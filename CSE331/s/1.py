grammer = {"S": "AB",
           "A":"CD,CF",
           "B":"c,EB",
           "C":"a",
           "D": "b",
           "E":"c",
           "F":"AD"
           }
word = "abcccc"

def cyk(grammer,word):
    g = {}
    for k,v in grammer.items(): #Making a dictionary where I will be able to search variables and terminals production variable
        for elm in v.split(","):
            if elm not in g.keys():
                g[elm] = k

            else:
                g[elm] = g[elm]+k

    #print(g)
    lst = []
    for elm in range(len(word)):#Making the dynamic array for CYK
        elm = len(word) - elm
        templst = []
        for i in range(elm):
            templst.append(None)
        lst.append(templst)
    #print(lst)
    for elm in range(len(word)):
        if elm == 0: #for first stage of cyk where we will convert the string to production variables
            count = 0
            for i in word: #going through the string
                lst[elm][count] = g[i]
                count += 1
        else: # this will work from the second to last stage of cyk 
            times = len(word) - elm # as in each stage the dynamic array gets smaller
            n = elm
            for k in range(times):
                temp = ""
                for i in range(n):
                    w1 = lst[i][k]#stair up 
                    w2 = lst[n-i-1][k+i+1] #stair down
                    w = ""
                    #print(i,k)
                    #print(n-i,k+i)
                    #print(w1,w2)
                    for a in w1:

                        if len(a) ==0:
                            continue


                        for b in w2:

                            if len(b) == 0:
                                continue
                            w += a+ b +"," #union 
                            
                    w = w.rstrip(",") #it contains the union of two dynamic indexes 
                    #print(w)

                        
                    temp += w + "," #total union 
                temp = temp.rstrip(",")
                temp = temp.split(",")
                ftemp = ""
                for a in temp:#going through it 
                    
                    if a in g.keys():
                        for i in g[a]:
                            if i not in ftemp: #handling duplicate cases
                                ftemp += i 
                            

                        
                lst[n][k] = ftemp #filling up upper indexes 

    print(lst)
    #print(lst[-1])
    x= lst[-1]
    if 'S' in x[0]:
        print("Possible")
    else:
        print("Not Possible")
                    

                
                







    #print(lst)



m = cyk(grammer,word)