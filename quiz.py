#Challenge 1 
def makes10(t,c): 

     if (t == 10 or c == 10 or t + c == 10 ):
     return True
    return ('False')

print(makes10(9,10))
print(makes10 (9,9))
print(makes10 (1,9))

#Challenge 2
def pos_neg(t,c, negative):
     if ( t > 0 and c < 0) or ( t < 0 and c > 0 ):
      return True 
     if (negative == True and t < 0  and c < 0 ):
    
      return True
     return False    
print(pos_neg(1,-1, False))  
print(pos_neg(-1,1, False)) 
print(pos_neg(4, 5, True )) 