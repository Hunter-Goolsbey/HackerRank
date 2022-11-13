#Sparse arrays challenge

def matchingStrings(stringList, queries):
  
    x = []
    
    for i in queries:
        c = 0
        
        for e in stringList:
            if i == e:
                c = c + 1
                
        x.append(c)

    return(x)
  
  
  
matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])
