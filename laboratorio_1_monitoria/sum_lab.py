# integrantes
# Andres feipe castrillon martinez (2380664)
# Johan Alexander Castro Zapata (2380818)
# santiago lopez ramirez  (2380798)


import random


# 1 sum the digits randoms number 
def sum_random():
    global first_sum, second_sum
    first_sum = 0
    for x in range(0,3):
        first_sum +=int(number[x])
        
        
    second_sum = 0
    for y in range(3,5):
        second_sum +=int(number[y])
   

if __name__ == '__main__':
    number=str(random.randint(10000, 99999))
    print("the random number is ", number)
    sum_random()
    
    
    if first_sum == second_sum:
        print(f"""the sum of the  {number[0:3]} = {first_sum}
           is equal to the sum of {number[3:5]} = {second_sum}""")
    else:
        print(f"""invalid check the sum of the  {number[0:3]} = {first_sum}
           it is not the same {number[3:5]} = {second_sum}""")
        

