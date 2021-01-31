#danielle Tuck
#section 2

#The purpose of this code is to display a random chess piece on the board and display
#the possible moves it could make according to chess rules

import random


# the chess piece super class
class ChessPiece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return (self.__x, self.__y)

    def x(self):
        return self.__x

    def y(self):
        return self.__y


class Pawn(ChessPiece):

    def pic(self):
        if self.color() == "w":
            return "\u2659"
        if self.color() == "b":
            return "\u265F"

    def validMove(self, x, y):
        if self.color() == "w":
            if self.y() == y + 1 and self.x() == x:
                return True
            else:
                return False
        if self.color() == "b":
            if self.y() == y - 1 and self.x() == x:
                return True
            else:
                return False


class Queen(ChessPiece):
    def pic(self):
        if self.color() == "w":
            return "\u2265"
        if self.color() == "b":
            return "\u265B"

    def validMove(self, x, y):
        if self.x() == x or self.y() == y:
            return True
        for i in range(-8, 8):
            if self.x() + i == x and self.y() + i == y:
                return True
            elif self.x() - i == x and self.y() + i == y:
                return True
        else:
            return False


class King(ChessPiece):
    def pic(self):
        if self.color() == "w":
            return "\u2654"
        if self.color() == "b":
            return "\u265A"

    def validMove(self, x , y):
        if self.x() -1 == x and self.y() == y:
            return True
        elif self.x() - 1 == x and self.y() -1 == y:
            return True
        elif self.x() + 1 == x and self.y() -1 == y:
            return True
        elif self.x() + 1 == x and self.y() +1 == y:
            return True
        elif self.x() == x and self.y() -1== y:
            return True
        elif self.x() -1 ==x and self.y() +1 ==y:
            return True
        elif self.x() ==x and self.y() +1 == y:
            return True
        elif self.x() +1 == x and self.y() == y:
            return True
        return False

class Rook(ChessPiece):
    def pic(self):
        if self.color() == "w":
            return "\u2656"
        if self.color() == "b":
            return "\u265C"

    def validMove(self, x, y):
        if self.x() == x or self.y() == y:
            return True
        else:
            return False

class Knight(ChessPiece):
    def pic(self):
        if self.color() == "w":
            return "\u2658"
        if self.color() == "b":
            return "\u265E"

    def validMove(self, x, y):
        if self.x() -2 == x and (self.y()-1 ==y or self.y()+1 ==y):
            return True
        elif self.y() + 2 == y and (self.x()-1 ==x or self.x()+1==x):
            return True
        elif self.x() +2 == x and (self.y()-1 ==y or self.y()+1 ==y):
            return True
        elif self.y() - 2 == y and (self.x()-1 ==x or self.x()+1==x):
            return True
        else:
            return False

class Bishop(ChessPiece):
    def pic(self):
        if self.color() == "w":
            return "\u2657"
        if self.color() == "b":
            return "\u265D"

    def validMove(self, x, y):
        for i in range(-8, 8):
            if self.x() + i == x and self.y() + i == y:
                return True
            elif self.x() - i == x and self.y() + i == y:
                return True
        return False


#Code below this line was the starter code given to me by my Professor


# print a nice picture of the valid moves
# white pawns only move "up" one space
# black pawns only move "down" one space
# other chess pieces move normally
def printValidMoves(cp):
    print("\t  ",  cp.pic(),  "at", cp.location())
    for i in range(7, -1, -1):
        print("\t" + str(i) + " ", end="")
        for j in range(0, 8):
            if cp.x() == j and cp.y() == i:
                print(cp.pic() + " ", end="")
            elif cp.validMove(j, i):
                print("* ", end="")
            else:
                print(". ", end="")
        print()
    print("\t  ", end="")
    for i in range(0, 8):
        print(str(i) + " ", end="")
    print()
    print()

# returns a random chess piece at a random location
# each of these types must inherit from ChessPiece
def randomChessPiece():
    if random.randint(0, 1) == 0:
        c = "w"
    else:
        c = "b"
    t = random.randint(1, 6)
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if t == 1: return Pawn(c, x, y)
    if t == 2: return Queen(c, x, y)
    if t == 3: return King(c, x, y)
    if t == 4: return Rook(c, x, y)
    if t == 5:
        return Knight(c, x, y)
    else:
        return Bishop(c, x, y)


def main():
    clist = []

    # make a list of random chess pieces
    for i in range(0, 10):
        clist.append(randomChessPiece())

    # display thier valid moves
    for i in range(0, len(clist)):
        printValidMoves(clist[i])

main()