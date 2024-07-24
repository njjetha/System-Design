class Players:
    def __init__(self, name):
        self.name = name
        # self.age = age
        # self.state = state
        # self.height = height
        self.runs = 0
        self.four = 0
        self.sixes = 0
        self.run_conceded = 0
        self.wickets = 0
        self.maiden = 0

    def batting_stat(self,runs):
        self.runs +=runs
        if(runs=='4'):
            self.four+=1
        if(runs == '6'):
            self.sixes+=1
    
    def bowling_stat(self,ball):
        if(ball == 'W'):
            self.wickets+=1
        else:
            self.run_conceded+=1
        