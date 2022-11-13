#Arrays-DS challenge

def reverseArray(a):
  
    x = []
    
    for i in range(len(a)-1, -1, -1):
        x.append(a[i])
        
    return(x)


reverseArray([1, 2, 3, 4, 5])
