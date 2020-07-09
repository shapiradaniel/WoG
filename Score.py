# Score.py

from Utils import SCORES_FILE_NAME
import os


# Function return the current score
def current_score():
    score = 0
    if os.path.exists(SCORES_FILE_NAME):
        score_fd = open(SCORES_FILE_NAME, "r")
        score = score_fd.read()
        score_fd.close()
        if not (score.isdecimal() and int(score) >= 0):
            score = 0
    return int(score)


# Function add score to the score file
def add_score(difficulty):
    points_of_winning = ((difficulty * 3) + 5) + current_score()
    score_fd = open(SCORES_FILE_NAME, "w")
    score_fd.write("%s" % points_of_winning)
    score_fd.close()
