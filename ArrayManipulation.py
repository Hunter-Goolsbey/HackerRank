#Array manipulation challenge


def arrayManipulation_1(n, queries):
  
    x = []

    for t in range(0,n):
        x.append(0)
    
    for i in queries:
        for e in range(i[0]-1,i[1]):
            x[e] = x[e]+i[2]
            
    return(max(x))
    


n = 5

queries = [[1,2,100],[2,5,100],[3,4,100]]

print(arrayManipulation_1(n, queries))
