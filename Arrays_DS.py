#Arrays-DS challenge

def reverseArray(a):
  
    x = []
    
    for i in range(len(a)-1, -1, -1):
        x.append(a[i])
        
    return(x)
