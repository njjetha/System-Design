class Cell:
    def __init__(self, number):
        self.number=number
        self.snake=None
        self.ladder=None
    def set_snake(self, snake):
        self.snake=snake
    def set_ladder(self, ladder):
        self.ladder=ladder

class Snake:
    def __init__(self, start, end):
        self.start=start
        self.end=end

class Ladder:
    def __init__(self, start, end):
        self.start=start
        self.end=end

class Board:
    def __init__(self):
        self.board=[Cell(i) for i in range(101) ]
