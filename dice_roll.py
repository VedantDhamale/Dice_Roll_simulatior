import random 
while True:     
     print('''\n 1. roll the dice \n 2. exit    \n ''')    
     user = int(input("what you want to do : \n"))     
     if user==1:         
        number = random.randint(1,6)         
        print("no on dicre is : ",number)     
     else:         
        break