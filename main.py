from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from random import*
from time import*

app = QApplication([])
from main_window import*
from menu_window import*

class Question():
    right_ans = 0
    count_ans = 0
    def __init__(self, question, answer, wrong_answer1, wrong_answer2 ,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
    def got_right(self):
        Question.right_ans +=1
        Question.count_ans +=1
    def got_wrong(self):
        Question.count_ans +=1











win_card.show()
app.exec_()