from Players import Players
class Teams:
    def __init__(self, players:list[Players]):
        # self.players = players
        self.players = players
        self.index = 1
        self.current_batsman = [0,1]
        self.runs = 0
        self.wickets = 0
    
    def next_batsman(self):
        next_player = max(self.current_batsman)+1
        self.wickets +=1
        if next_player>=len(self.players):
            print ("All OUT !!!!")
            return
        self.current_batsman.pop(0)
        self.current_batsman.insert(0,next_player)
    
    def change_strike(self):
        self.current_batsman.reverse()
    
    def team_score(self, runs):
        self.players[self.current_batsman[0]].batting_stat(runs)
        self.runs+=runs
