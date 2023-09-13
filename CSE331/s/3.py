import itertools


grammer = {"S": "AB",
           "A":"CD,CF",
           "B":"c,EB",
           "C":"a",
           "D": "b",
           "E":"c",
           "F":"AD"
           }
word = "abcccc"

def CYK_Algo(grammer,word):
    new_grammer = {}
    for key,val in grammer.items():
        for elm in val.split(","):
            if elm not in new_grammer.keys():
                new_grammer[elm] = key
            else:
                new_grammer[elm] += key
    print(new_grammer)
    
    #Now we will make the 2d dynamic list 
    
    lst = []
    length = len(word)
    for elm in range(length-1,-1,-1):
        lst.append([])
        for i in range(elm+1):
            lst[-1].append([])
    
    

    #Now we will change the first index of dynamic array using the given string
    count = 0
    for elm in word:
        d = new_grammer[elm]
        for selm in d:
            lst[0][count].append(selm)
        count += 1
    print(lst)

    # # Lets do it for the rest of the dynamic array 

    for elm in range(1,length):
        for selm in range(length-elm):
            t_lst = []
            for melm in range(elm):
                index1 = lst[melm][selm]
                index2 = lst[elm-melm-1][selm+melm+1]
                index3 = list(itertools.product(index1,index2))
                print(index3)
                t_lst.append(index3)
            
            new_index = []
            for ss in t_lst:
                for u in ss:
                
                    if len(u) ==0:
                        continue
                    u1,u2 = u
                    
                    if len(u1)==0 or len(u2)==0:
                        pass
                    else:
                        print(u1,u2)

                        uk = u1 + u2
                        print(uk)
                        if uk in new_grammer.keys():
                            ug = new_grammer[uk]
                            print(ug)
                            
                            new_index.append(ug)
            for b in new_index:
                
                for cc in b:
                    if cc not in lst[elm][selm]:
                        lst[elm][selm].append(cc)
    print(lst)


g = CYK_Algo(grammer,word)
