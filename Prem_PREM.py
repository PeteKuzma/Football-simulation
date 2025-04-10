import numpy as np  
from premierleague_fncs import *
import re   
from functools import reduce
import functools
import _pickle as cpk

# list of (team, strength) tuples:

fopen=open("/Users/peteKuzma/Documents/Software/EPL/premlist.pickle",'rb')
teams=cpk.load(fopen)
fopen.close()


# build list of 3-letter versions of team names to be
# used as unique IDs:
#ids = createShortNames(teams) 
ids=[]
id2team=dict()

for i in range(len(teams)):
    ids.append(teams[i][3])
    id2team[teams[i][3]]=teams[i][0:3]


# build a dictionary where each key is a short name (ID)
# and the corresponding value is a
# (full team name, strength) tuple:
#id2team = dict( zip(ids, teams) )

# build a dictionary representing the match board:
matchboard = initializeMatchBoard(ids)

# build a dictionary such that each team ID is
# associated with a tuple of 7 integers representing
# played matches, matches won, matches drawn,
# matches lost, goals scored, goals received, and points
stats = dict([(id, [0]*21) for id in ids])
mb=np.array((0,1,2,5,10,19,30,32,34,35,36,37))
final_games=np.array((30,32,34,35,36,37))

total_rounds=38
total_teams=20
total_gpr=10

# Play full tournament:
# The teams play each other twice. 
# 3 points for a win, 1 for a draw, 0 for a loss
#Creating fixtures
sch=create_schedule_FULL(ids)

Total_fixtures_list=sch

# Begin counting matches
matches=0
i=0
for i in range(total_rounds):
    matches=i+1
    Round=Total_fixtures_list[i]
    for b in range(len(Round)):
    # simulates the matches
        strengthA=id2team[Round[b][0]][1]
        strengthB=id2team[Round[b][1]][2]
        sAw=id2team[Round[b][0]][2]
        sBh=id2team[Round[b][1]][1]
        if isinstance(strengthA,str)==True:
            print("True")
            strengthA=int(strengthA)
            strengthB=int(strengthB)
            strengthA=int(sAw)
            strengthB=int(sBh)
        goalsA, goalsB = playMatch(strengthA, strengthB,sAw,sBh)
        resultstring = "%d-%d"%(goalsA, goalsB)
        matchboard[(Round[b][0], Round[b][1])] = resultstring
    for j in range(total_gpr):
        # Updates the leaderboard and stores the stats.
        #print("Round: {0}, game: {1}".format(i+1,j+1))
        teamA=Round[j][0]
        teamB=Round[j][1]
        score=matchboard[(teamA,teamB)]
        #print("{0} VS. {1}: {2}".format(teamA,  teamB, score))
        goalsA=int(re.findall(r'\d+',score)[0])
        goalsB=int(re.findall(r'\d+',score)[1])
        if goalsA > goalsB:          # team A won
            updateWinner(teamA, stats,"home")
            updateLoser(teamB, stats,"away")
        elif goalsA < goalsB:        # team B won
            updateWinner(teamB, stats,"away")
            updateLoser(teamA, stats,"home")
        else:                        # draw
            updateDraw(teamA, teamB, stats)
        updateMatch(teamA, goalsA, teamB, goalsB, stats)
    if i in mb:
        if i in final_games:
            for j in range(total_gpr):
                print("Round: {0}, game: {1}".format(i+1,j+1))
                teamA=Round[j][0]
                teamB=Round[j][1]
                score=matchboard[(teamA,teamB)]
                print("{0} VS. {1}".format(id2team[teamA][0],  id2team[teamB][0], score,))
                #gh=input()
                print(score)
                print("----------------")
        exec(open("./table_test.py").read())
        #input("Enter to continue")

fopen=open("/Users/petekuzma/Documents/Software/EPL/prem.pickle",'wb')
cpk.dump(ranking,fopen)
fopen.close()