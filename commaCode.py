# Comma Code 1-4a

# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an 
# argument and returns a string with all the items 
# separated by a comma and a space, with and inserted 
# before the last item. For example, passing the 
# previous spam list to the function would return 
# 'apples, bananas, tofu, and cats'. But your 
# function should be able to work with any list 
# value passed to it. 

def commaCode(myList) :
    # take list as an input
    # return a string of items seperated by ' ,'
    # only operates on 1d lists

    myString = "" # start building the return string

    # if the list is empty return an empty string
    if len(myList) == 0 :
        return(myString)

    # load in the first item from the string
    myString = str(myList[0])

   # if the list is a lone item, return that item
    if len(myList) == 1 :
          return(myString)

 
    # loop through remainin myList until 1 before the end
    for i in myList[1:-1] :
        myString += ", " + str(i)

    # add the last item with the an 'and'
    myString += " and " + str(myList[-1])

    return(myString)


# Main section of code

spam = ['apples', 'bananas', 'tofu', 'cats']
print(spam)
print(commaCode(spam))
print()

spam = [] # test  empty list
print(spam)
print(commaCode(spam))
print()

spam = ["Test one item"]
print(spam)
print(commaCode(spam))
print()

spam = ["Test one item", "another"]
print(spam)
print(commaCode(spam))
print()