"""

Problem-4: Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
(examples)
input: [1,2,8,9,12,46,76,82,15,20,30]
Output:
{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}


"""


a = input().split(",") #input example : 1,2,8,9,12,46,76,82,15,20,30 

numcount = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
 }

for i in a:
    
    # Checking count of 1 divisibles 
    if int(i)%1 == 0:
        numcount[1] += 1
        
    # Checking count of 2 divisibles    
    if int(i)%2 == 0:
        numcount[2] += 1
        
    # Checking count of 3 divisibles    
    if int(i)%3 == 0:
        numcount[3] += 1
        
    # Checking count of 4 divisibles    
    if int(i)%4 == 0:
        numcount[4] += 1
        
    # Checking count of 5 divisibles    
    if int(i)%5 == 0:
        numcount[5] += 1
        
    # Checking count of 6 divisibles    
    if int(i)%6 == 0:
        numcount[6] += 1
        
    # Checking count of 7 divisibles    
    if int(i)%7 == 0:
        numcount[7] += 1
        
    # Checking count of 8 divisibles    
    if int(i)%8 == 0:
        numcount[8] += 1
        
    # Checking count of 9 divisibles    
    if int(i)%9 == 0:
        numcount[9] += 1
          
        
print(numcount)
