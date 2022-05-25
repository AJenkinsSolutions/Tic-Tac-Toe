#Break grid up into alpha numberic section based on row and column
#The box in the upper right hand corner will be box = A0,
#The box immediatly to its right will be B0

#The the next box C0
# a0, b0, c0
# a1, b1 ,c1
# a2, b2, c2

#each box will be a string:
# artString = spaces " " and "|" *This is what creates the visuals*
# Within the string repersetnation of our box will lie a center 'piece'
# This center piece will be the part of th string we will replace
# with the corrosponding player pawn "X" OR "O">
#              pawn_A = "X"
#              pawnn_B = "O"

#The game will consist of two players:
#          player_A and player_B

#Each player will be given a Pawn style:
#               "X" or "O"

#Players will take it in turns
#            *onscreen acsii art*


#In order to place pawn on screen they must select a box:
                    # a0, b0, c0
                    # a1, b1 ,c1
                    # a2, b2, c2

# Apon selecting a box if valid, player pawn will be place on screen in selected Box

#Using algo th winner will be the first to connect three pawns on
#                  Horizontal_Win
#                  Vertical_Win
#                  Diagonal_Win_A
#                  Diagonal_Win_B


#**Horizontal wins**
# 3 pawns from left to right
# conditions
# 1: pawn located only 1 or these:  a0, a1, a2, c0, c1, c2
#             *These are all the ar edges*
# 2: pawn located in adjcent middle:
#          *example, 1st box== a0 : pawnmust be at b0*
# 3: pawn located outer edge:
#          *example, 2nd box==b0: pawnmust be at c0*
#if all conditons are met declare winner


# pawn can be placed function
#  take players input box selection input
#  run that through a func that goes into the current grid picture art
#  if pawn_present deny the move and make player chose again
#  if pawn_present  == false place player pawn in location
#  then print the new grid to the screen

# swith players turn


a = """
         |     |     
      X  |  -  |  -  
    _____|_____|_____
         |     |     
      -  |  O  |  X  
    _____|_____|_____
         |     |     
      -  |  O  |  -  
         |     |
         """
print(a)