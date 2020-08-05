# Chess Dictionary Validator 1-5a
# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 
# 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent
# a chess board. Write a function named isValidChessBoard() that takes 
# a dictionary argument and returns True or False depending on if the 
# board is valid.

# A valid board will have exactly one black king and exactly one white 
# king. Each player can only have at most 16 pieces, at most 8 pawns, 
# and all pieces must be on a valid space from '1a' to '8h'; that is, a 
# piece can’t be on space '9z'. The piece names begin with either a 'w' 
# or 'b' to represent white or black, followed by 'pawn', 'knight', 
# 'bishop', 'rook', 'queen', or 'king'. This function should detect when 
# a bug has resulted in an improper chess board.

# board format to match standard chess annotation 
# (this could be improved to a 2D list?)
# 8a, 8b, 8c, 8d, 8e, 8f, 8g, 8h
# 7a, 7b, 7c, 7d, 7e, 7f, 7g, 7h
# 6a, 6b, 6c, 6d, 6e, 6f, 6g, 6h
# 5a, 5b, 5c, 5d, 5e, 5f, 5g, 5h
# 4a, 4b, 4c, 4d, 4e, 4f, 4g, 4h
# 3a, 3b, 3c, 3d, 3e, 3f, 3g, 3h
# 2a, 2b, 2c, 2d, 2e, 2f, 2g, 2h
# 1a, 1b, 1c, 1d, 1e, 1f, 1g, 1h

# pieces descibed as 
# prefix 'b' as black and 'w' as white
# postfix as 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
# (this could be improved to a 2chr code B/W & P/N/B/R/Q/K ?)

def isValidChessBoard(myBoard) :
    # takes a chess board and validates the following
    # exactly 1 'bking', 'wking'
    # max 16 'b..' or 'w..' pieces
    # max 8 'bpawn', 'wpawn'
    # all pieces are on a valid square
    # return True for valid, and False for invalid board
    debugMe = False

    # key validation
    # check all keys fall within a-h and 1-8
    # structure enforces unique keys
    for k in myBoard.keys() :
        
        #check key is 2 chr long
        if (len(k) != 2) :
            if (debugMe) : print("Key too long", k)
            return(False)
 
        #check 1st char is 1-8
        if (k[0] < '1') or (k[0] > '8') :
            if (debugMe) : print("Bad rank position", k)
            return(False)
            
       #check 2nd char is a-h
        if (k[1] < 'a') or (k[1] > 'h') :
            if (debugMe) : print("Bad file position", k)
            return(False) # Invalid file (column position)

    
    # piece validation
    # load all pieces into a list (pCount) with count for each
    pCount = {}
    for v in myBoard.values() :
        pCount.setdefault(v,0) # avoids error on next line with new pieces
        pCount[v] += 1 # increment count of piece
        
    if (debugMe) : print(pCount)

    # check kings
    if (pCount.get('bking',0) != 1 ) : # check for black king
        if (debugMe) : print("Incorrect # Black Kings")
        return(False)

    if (pCount.get('wking',0) != 1 ) : # check for black king
        if (debugMe) : print("Incorrect # Black Kings")
        return(False)

    # check pawns
    if (pCount.get('bpawn',0) > 8 ) : # check for black pawns
        if (debugMe) : print("Excessive Black Pawns")
        return(False)

    if (pCount.get('wpawn',0) > 8 ) : # check for white pawns
        if (debugMe) : print("Excessive White Pawns")
        return(False)
   

    # count number of pieces for each side
    sCount = {}
    for k, v in pCount.items() :
        if (len(k)>0) : # not an empty square
            side = k[0] # b/W
            sCount.setdefault(side,0) # only uses 1st char in each piece name
            sCount[side] += v # increment count by number of pieces

    if (debugMe) : print(sCount)
        
    if (sCount['b'] > 16) : 
        if (debugMe) : print("Too many black pieces", sCount['b'])
        return(False)
    
    if (sCount['w'] > 16) :
        if (debugMe) : print("Too many white pieces", sCount['w'])
        return(False)


    return(True) # all validation checks have been passed




# main code block
startingBoard = { '8h' : 'brook',
                  '8b' : 'bknight',
                  '8c' : 'bbishop',
                  '8d' : 'bqueen',
                  '8e' : 'bking',
                  '8f' : 'bbishop',
                  '8g' : 'bknight',
                  '8h' : 'brook',

                  '7a' : 'bpawn',
                  '7b' : 'bpawn',
                  '7c' : 'bpawn',
                  '7d' : 'bpawn',
                  '7e' : 'bpawn',
                  '7f' : 'bpawn',
                  '7g' : 'bpawn',
                  '7h' : 'bpawn',

                  '6a' : '',
                  '6b' : '',
                  '6c' : '',
                  '6d' : '',
                  '6e' : '',
                  '6f' : '',
                  '6g' : '',
                  '6h' : '',
                  
                  '5a' : '',
                  '5b' : '',
                  '5c' : '',
                  '5d' : '',
                  '5e' : '',
                  '5f' : '',
                  '5g' : '',
                  '5h' : '',
                
                  '4a' : '',
                  '4b' : '',
                  '4c' : '',
                  '4d' : '',
                  '4e' : '',
                  '4f' : '',
                  '4g' : '',
                  '4h' : '',
            
                  '3a' : '',
                  '3b' : '',
                  '3c' : '',
                  '3d' : '',
                  '3e' : '',
                  '3f' : '',
                  '3g' : '',
                  '3h' : '',

                  '2a' : 'wpawn',
                  '2b' : 'wpawn',
                  '2c' : 'wpawn',
                  '2d' : 'wpawn',
                  '2e' : 'wpawn',
                  '2f' : 'wpawn',
                  '2g' : 'wpawn',
                  '2h' : 'wpawn',

                  '1a' : 'wrook',
                  '1b' : 'wknight',
                  '1c' : 'wbishop',
                  '1d' : 'wqueen',
                  '1e' : 'wking',
                  '1f' : 'wbishop',
                  '1g' : 'wknight',
                  '1h' : 'wrook'}
                  
if (isValidChessBoard(startingBoard) == True) :
    print ("Valid board")
else :
    print ("Warning - invalid board")
