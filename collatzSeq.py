#The Collatz Sequence 
# Training project from automateTheBoringStuff.com
# a function named collatz() that has one parameter 
# named number. If number is even, then collatz() 
# should print number // 2 and return this value. 
# If number is odd, then collatz() should print and 
# return 3 * number + 1.

#known issues - negative integers are not solveable

def getIntFromUser() :
  while True :
    try : 
        return(int(input ("Please enter an interger : ")))
    except ValueError :
        print("That wasn't recognised as an integer. [Invalid Input]")

def collatz(number) :
    # Take integer as input

    # if Even, div2 and return
    # if odd, *x+1 and return

    # verify that the input to the function is valid
    if int(number) : # if the input is an interger

        if number %2 == 0 : # even number
            return( int(number/2) )
        else: # assumes !even = odd
            return( int(number*3+1) )
    else:
        return (None) # invalid input response

# take user input
print ("Welcome to the Collatz Sequence")
print ("From automatetheboringstuff.com")
print ("")

letsRepeat = "y"
while letsRepeat == "y" :

    # get a valid int from user
    print("What is the starting number for the sequence?")
    number = getIntFromUser ()

    # show back the initial condition for the sequence
    print("\nStarting sequence with", number)

    while number != 1 : # 1 ends the sequence
        print(number) # show current number
        number = collatz(number) # update to next number
    
    # last number not shown above
    print("1\nand the end of the sequence\n") 

    # check if the user wants to repeat the sequence
    letsRepeat = input("\nDo you want to try a new sequence? 'y' to repeat :")