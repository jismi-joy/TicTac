# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request
import re

from PlayGame import PlayGame

app = Flask(__name__)


def validate_board(board):
    ret = True
    for piece in board:
        if piece == 'x':
            continue;
        elif piece == 'o':
            continue;
        elif piece == ' ':
            continue
        else:
            ret = False
            break
    return ret

@app.route("/")
def home():
    board = request.args.get('board')
    try:
        if not validate_board(board):
            return "Invalid board", 400
        Game = PlayGame()
        result = Game.playGame(board)
        if result == "":
            return "Invalid board", 400
    except:
        return "Invalid board", 400

    return result

if __name__ == "__main__":
    app.run()
    '''
    Game = PlayGame()
    result = Game.playGame("xox     o")
    print(result)
    '''


