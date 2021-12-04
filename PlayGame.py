import re

from Board import Board


class PlayGame:
    boardstring = ""
    board = Board()
    player = "o"
    opponent = "x"

    def getOutputString(self, str, pos):
        print(pos)
        newstr = str[:pos] + self.player + str[pos + 1:]
        #self.boardstring = newstr.replace("+", " ")
        return newstr


    def playGame(self, str):
        # result string added o
        newstr = ""
        # check if the board is filled
        if not self.isValid(str):
            print("not valid")
            newstr = "invalid string", 400
            return newstr

        # check if the board is empty, then fill the centre
        if self.isEmpty(str):
            newstr = "    "+self.player+"    "
            return newstr

        # create board using the string
        self.board.create_board(str)

        # find the winning position if there is any
        win = self.winningPos()

        if win is not None:
            return self.getOutputString(str, win)

        # find the blocking position if there is any
        block = self.blockingPos()
        if block is not None:
            return self.getOutputString(str, block)

        # find the fork position if there is any
        fork = self.forkPos()
        if fork is not None:
            return self.getOutputString(str, fork)

        # find the fork block position if there is any
        blockfork = self.forkBlockPos()
        if blockfork is not None:
            return self.getOutputString(str, blockfork)

        # find the corner position if there is any
        cornerpos = self.board.getCornerPosition()
        if cornerpos is not None:
            return self.getOutputString(str, cornerpos)

        # find the empty corner position if there is any
        emptyCorner = self.board.getEmptyCornerPosition()
        if emptyCorner is not None:
            return self.getOutputString(str, emptyCorner)

        # find the empty side position if there is any
        emptySide = self.board.getEmptySidePosition()
        if emptySide is not None:
            return self.getOutputString(str, emptySide)
        return newstr

    def isEmpty(self, str):
        if str == "         ":
            return True
        else:
            return False

    def isValid(self, boardstring):
        print(boardstring)
        #find if the boardstring contains any space
        res = bool(re.search(r"\s", boardstring))
        if len(boardstring) != 9:
            print("string length not correct")
            return False
        elif boardstring.count(self.player) > boardstring.count(self.opponent) or boardstring.count(self.opponent) > boardstring.count(self.player) + 1:
            print("not players move")
            return False
        elif len(boardstring) == 9 and str(res) == False:
            print("Game over")
            return False
        else:
            return True

    def winningPos(self):
        return self.board.getWinBlockPos(self.player)

        # find the blocking position if there is any

    def blockingPos(self):
        return self.board.getWinBlockPos(self.opponent)

        # find the fork position if there is any

    def forkPos(self):
        return self.board.getForkBlockPos(self.player)

        # find the blockfork position if there is any

    def forkBlockPos(self):
        return self.board.getForkBlockPos(self.opponent)
