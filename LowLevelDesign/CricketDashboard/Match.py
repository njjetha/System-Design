from Teams import Teams
from Players import Players
class Match:
    def __init__(self, TeamA:Teams, TeamB:Teams):
        self.batting = TeamA
        self.bowling = TeamB
        self.bowler= None
        self.overs = None
    
    
    def over_stat(self, bowler:Players, overs:list):
        self.bowler=bowler
        self.overs=overs
        runs_over=0
        for ball in self.overs:
            self.bowler.bowling_stat(ball)
            if ball == 'W':
                self.batting.next_batsman()
            elif ball == 'Wd':
                runs_over+=1
                self.batting.team_score(1)
            else:
                runs_over+=int(ball)
                self.batting.team_score(int(ball))
        self.batting.change_strike()
        if runs_over == 0:
            self.bowler.maiden+=1
    

    def result(self, teamA:Teams, teamB:Teams):
        if teamA.runs > teamB.runs:
            print(f"Team A won the match by {teamA.runs - teamB.runs}")
        elif teamA.runs < teamB.runs:
            print(f"Team B won the match by {teamB.runs - teamA.runs}")
        else:
            print ("Match Tied ...........")
    
    def inning_break(self, teamA:Teams, teamB:Teams):
        self.batting=teamB
        self.bowling=teamA


if __name__ == '__main__':
    p1=Players("P1")
    p2=Players("P2")
    p3=Players("P3")
    p4=Players("P4")
    p5=Players("P5")
    p6=Players("P6")
    teamA=Teams([p1,p2,p3])
    teamB=Teams([p3,p4,p5])
    print("Batting Choosen by TeamA .....") # hardcoded
    match=Match(teamA, teamB)
    match.over_stat(p3, ["1", "0", "1", "W", "6", "2"])
    print(f"Total target set by team A {teamA.runs}")
    print("Inning Break .....")
    
    match.inning_break(teamA, teamB)
    match.over_stat(p2,["6","2","4","1","1","2"])
    match.result(teamA, teamB)

    

            

