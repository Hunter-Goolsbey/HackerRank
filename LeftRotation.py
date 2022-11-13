#Rotate array to the left challenge

def rotateLeft(d, arr):
    
    z = []
    
    for i in range(-1 * (len(arr) - d), d):
        z.append(arr[i])
        
    return(z)
  
  
rotateLeft(4, [1, 2, 3, 4, 5])
