class Board:
    matrix = [[0 for i in range(3)] for i in range(3)]
    opponent = "x"
    def create_board(self, str):
        print("creating board")
        x = 0
        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = str[x]
                x = x + 1

    ''' 
    get win or block position for o.
    win position for x is block position for o 
    '''

    def getWinBlockPos(self, ch):
        print("get win block position")
        num = 0
        pos = None
        find = False

        # check all the raws
        for i in range(3):
            num = 0
            find = False
            for j in range(3):
                if (self.matrix[j][i] == ' '):
                    pos = j * 3 + i
                    find = True
                elif (self.matrix[j][i] == ch):
                    num = num + 1
                else:
                    break;

            if (num == 2 and find == True):
                return pos

        # check colomns
        for i in range(3):
            num = 0
            find = False
            for j in range(3):
                if (self.matrix[i][j] == ' '):
                    pos = i * 3 + j
                    find = True
                elif (self.matrix[i][j] == ch):
                    num = num + 1
                else:
                    break;
            if (num == 2 and find == True):
                return pos

        # check diagonal left to right
        num = 0
        find = False
        for i in range(3):
            if self.matrix[i][i] == ' ':
                pos = i * 3 + i
                find = True
            elif self.matrix[i][i] == ch:
                num = num + 1
            else:
                break;
            if (num == 2 and find == True):
                return pos

        # check diagonal right to left
        num = 0
        find = False
        for i in range(3):
            if self.matrix[2 - i][i] == ' ':
                pos = (2 - i) * 3 + i
                find = True
            elif (self.matrix[2 - i][i] == ch):
                num = num + 1
            else:
                break;
        if (num == 2 and find == True):
            return pos
        return None

    # get fork position for o and Blocking an x's fork
    def getForkBlockPos(self, ch):
        print("get blocking position")
        pos = None

        for i in range(3):
            for j in range(3):
                num = 0
                if self.matrix[i][j] == ' ':
                    if (i - 2 >= 0):
                        if self.matrix[i - 2][j] == ch:
                            num = num + 1
                    if (i - 1 >= 0):
                        if self.matrix[i - 1][j] == ch:
                            num = num + 1
                    if (i + 1 <= 2):
                        if self.matrix[i + 1][j] == ch:
                            num = num + 1
                    if (i + 2 <= 2):
                        if self.matrix[i + 2][j] == ch:
                            num = num + 1
                    if (j - 2 >= 0):
                        if self.matrix[i][j - 2] == ch:
                            num = num + 1
                    if (j - 1 >= 0):
                        if self.matrix[i][j - 1] == ch:
                            num = num + 1
                    if (j + 1 <= 2):
                        if self.matrix[i][j + 1] == ch:
                            num = num + 1
                    if (j + 2 <= 2):
                        if self.matrix[i][j + 2] == ch:
                            num = num + 1
                    if (num == 2):
                        pos = i * 3 + j
                        return pos
        return None

    def getCornerPosition(self):
        print("get corner position")
        pos = None
        if (self.matrix[0][0] == self.opponent and self.matrix[2][2] == " "):
            pos = 8
            return pos

        if (self.matrix[0][2] == self.opponent and self.matrix[2][0] == " "):
            pos = 6
            return pos

        if (self.matrix[2][0] == self.opponent and self.matrix[0][2] == " "):
            pos = 2
            return pos

        if (self.matrix[2][2] == self.opponent and self.matrix[0][0] == " "):
            pos = 0
            return pos

        return None

    def getEmptyCornerPosition(self):
        print("get empty corner position")
        pos = None
        if self.matrix[0][0] == " ":
            pos = 0
            return pos

        if self.matrix[0][2] == " ":
            pos = 2
            return pos

        if self.matrix[2][0] == " ":
            pos = 6
            return pos

        if self.matrix[2][2] == " ":
            pos = 8
            return pos

        return None

    def getEmptySidePosition(self):
        print("get empty side position")
        pos = None
        if self.matrix[0][1] == " ":
            pos = 0
            return pos

        if self.matrix[1][0] == " ":
            pos = 2
            return pos

        if self.matrix[2][1] == " ":
            pos = 6
            return pos

        if self.matrix[1][2] == " ":
            pos = 8
            return pos

        return None
