import random

OurRandomNumber = random.randrange(1,101)

print("Welcome to the Gussing Number Game !")

while True:

    try:
        TheGuss =  input("Guss The Number Between [1 - 100] > ")
        TheGuss = int(TheGuss)

        if TheGuss > 0 and TheGuss < 101:
         
            if TheGuss == OurRandomNumber:
                print("")
                print("Correct !")
                print("The Number was ", OurRandomNumber , " !")
                break
            elif TheGuss > OurRandomNumber : 
                print("Lower")
            elif TheGuss < OurRandomNumber :
                print("Higher")
        else:
            print("Thats Not A Number Between [1 - 100]")
        
    except ValueError:
        print("This is not a Number")
    
    

   