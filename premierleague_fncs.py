from random import randrange, gauss
import operator
import numpy as np
from functools import reduce
import random

def createShortNames(teams):
    """Return new list of unique, 3-letter
    abbreviations of all the names in the given list"""

    shortnames = []

    for team, strengtha,strengthb in teams:
        words = team.split()
        if len(words) > 1:
            s = words[0][:2] + words[1][0]
        else:
            s = words[0][:3]

        while s in shortnames:
            s = input("""Enter 3-letter name
            for %s not in %s"""%(team, shortnames))
        shortnames.append(s)

    return shortnames



def longestName(length, teamtuple):
    """Return maximum of given length and given team's
    name, where team is a (team name, strength) tuple"""
    
    return max(length, len(teamtuple[0]))



def initializeMatchBoard(ids):
    """Return dictionary representing an initialized
    match board holding all results of all matches among
    the teams from the given list of team IDs.

    Each key is a tuple (team1, team2), and the
    corresponding value is the string '   '. Each time a
    match is played between two teams, the corresponding
    entry should be updated with the result. Think of it
    as a large table (here with teams A, B, C):

       A  B  C
    A  x  x  x
    B  x  x  x
    C  x  x  x  (each x is a 3-space string)"""
    
    # use list comprehension 
    matchboard_keys = [(a, b) for a in ids for b in ids] 
    return dict.fromkeys( matchboard_keys, '   ' )


def playMatch(a, b, aw, bh, total_goals = 9):
    """Play a match between two teams with the given
    strengths. Return the tuple (ga, gb) of the number
    of goals scored by a and b, respectively, where A 
    is the home team and b is the away team. """
    # between 0 and total_goals per match:
    goals = int(min(total_goals, max(0, gauss(3, 2)))) 
    goals_a = goals_b = 0
    # Introduces a random effect to simulate the unpredicatbility
    # of the game. The are 10 effects based on a random number
    # between 0 and 9.
    a_bonus=random.randrange(10)
    b_bonus=random.randrange(10)
    #print("A_bouns= {0}, B_bonus {1}".format(a_bonus,b_bonus))
    if a_bonus==0:
        b=0
        #print("A_bonus of zero")
    elif a_bonus==1:
        b=b+random.randrange(-2,2)
        #print("A_bonouse")
    elif a_bonus==2:
        a=a+1
        #print("A_bonus of two")
    elif a_bonus==3:
        b=b-3
        #print("A_bonus of three")
    elif a_bonus==5:
        a=a+(bh-aw)
        #print("A_bonus of 5")
    elif a_bonus==6:
        a=a-1
        #print("A_bonus of 6")
    elif a_bonus==7:
        a=a+a%4
        #print("A_bonus of 7")
    elif a_bonus==8:
        a=a-a%4
        #print("A_bonus of 8")
    elif a_bonus==9:
        a=aw
        #print("A_bonus of 9")
    elif a_bonus==4:
        a_bonus=b_bonus
        #print("A_bonus of 9")
        if a_bonus==0:
            b=0
        elif a_bonus==1:
            b=b+random.randrange(-2,2)
        elif a_bonus==2:
            a=a+1
        elif a_bonus==3:
            b=b-3
        elif a_bonus==5:
            a=a+(bh-aw)
        elif a_bonus==6:
            a=a-1
        elif a_bonus==7:
            a=a+a%4
        elif a_bonus==8:
            a=a-a%4
        elif a_bonus==9:
            a=aw
        else:
            a=b
    else:
        a=a
    if b_bonus==0:
       a=0
    elif b_bonus==1:
        a=a+random.randrange(-2,2)
    elif b_bonus==2:
        b=b+1
    elif b_bonus==3:
        a=a-3
    elif b_bonus==5:
        b=b+(aw-bh)
    elif b_bonus==6:
        b=b-1
    elif b_bonus==7:
        b=b+b%4
    elif b_bonus==8:
        b=b-b%4
    elif b_bonus==9:
        b=bh
    elif b_bonus==4:
        b_bonus=a_bonus
        if b_bonus==0:
            a=0
        elif b_bonus==1:
            a=a+random.randrange(-2,2)
        elif b_bonus==2:
            b=b+1
        elif b_bonus==3:
            a=a-3
        elif b_bonus==5:
            b=b+(aw-bh)
        elif b_bonus==6:
            b=b-1
        elif b_bonus==7:
            b=b+b%4
        elif b_bonus==8:
            b=b-b%4
        elif b_bonus==9:
            b=bh
        else:
            b=a
    else:
        b=b
    a=np.clip(a,0,1000)
    b=np.clip(b,0,1000)
    #totalstrength = a + b
    #print("total Strengrth test:",totalstrength)
    #try:
    #    for i in range(goals):
    #        if randrange(totalstrength) < a:
    #            goals_a += 1
    #        else:
    #            goals_b += 1
    #except:
    #    goals_a=0
    #    goals_b=0
    goals_a=a
    goals_b=b
    return goals_a, goals_b



def sorttuples(a, b):
    """a and b are key/value dictionary items, i.e.
    (id, T), where id is a team ID and T is its match
    statistics tuple.
    
    Return 1, 0 or -1 depending on whether a should come
    before b when sorted accoring to the match
    statistics of the two teams."""

    A = a[1]
    B = b[1]
    
    if A[6] > B[6]:
        return -1

    elif A[6] < B[6]:
        return 1

    elif A[4]-A[5] > B[4]-B[5]:
        return -1

    elif A[4]-A[5] < B[4]-B[5]:
        return 1

    elif A[4] > B[4]:
        return -1

    elif A[4] < B[4]:
        return 1

    else:
        return 0
 
def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 



def updateWinner(id, stats,location):
    """The team given by the id has won a match;
    update stats accordingly."""
    stats[id][1] += 1  # matches won
    stats[id][6] += 3  # points
    if location=="home":
        stats[id][8]+=1 # matches won home
        stats[id][13]+=3
    if location=="away":
        stats[id][15]+=1 # matches won away
        stats[id][20]+=3               


def updateLoser(id, stats,location):
    """The team given by the id has lost a match;
    update stats accordingly."""
    stats[id][3] += 1  # matches won
    if location=="home":
        stats[id][10]+=1 # matches won home
    if location=="away":
         stats[id][17]+=1 # matches won away
        


def updateDraw(idA, idB, stats):
    """The two given teams have drawn a match,
    update stats accordingly."""

    stats[idA][2] += 1 # matches drawn
    stats[idA][6] += 1 # points
    stats[idB][2] += 1 # matches drawn
    stats[idB][6] += 1 # points 
    stats[idA][9] += 1 # matches drawn (home)
    stats[idA][13] += 1 # points
    stats[idB][16] += 1 # matches drawn (away)
    stats[idB][20] += 1 # points    


def updateMatch(idA, goalsA, idB, goalsB, stats):
    """Update stats for teams A and B according
    to the match just played in which A scored
    goalsA and B scored goalsB goals."""

    stats[idA][0] += 1      # matches
    stats[idA][4] += goalsA # goals scored by A
    stats[idA][5] += goalsB # goals received by B
    stats[idA][7] += 1      # matches (home)
    stats[idA][11] += goalsA # goals scored by A
    stats[idA][12] += goalsB # goals received by B
    stats[idB][0] += 1      # matches
    stats[idB][4] += goalsB # goals scored by B
    stats[idB][5] += goalsA # goals scored by A
    stats[idB][14] += 1      # matches (home)
    stats[idB][18] += goalsB # goals scored by A
    stats[idB][19] += goalsA # goals received by B


def create_schedule(list2):
    """ Create a schedule for the teams in the list and return it"""
    s = []
    if len(list2) % 2 == 1: list2 = list2 + ["BYE"]
    for i in range(len(list2)-1):
        mid = len(list2) / 2
        l1 = list2[:int(mid)]
        l2 = list2[int(mid):]
        l2.reverse()    
        # Switch sides after each round
        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]
        list2.insert(1, list2.pop())
    return s

def create_schedule_FULL(list2):
    s=[]
    for i in range(len(list2)):
        team=list2[i]
        idws=np.copy(list2)
        idws=idws[idws!=team]
        for k in range(len(idws)):
            s.append((team,idws[k]))
    random.shuffle(s)
    FS=[]
    for i in range(2*len(list2)-2):
        FS.append(s[0+int(i*(len(list2)/2)):int((len(list2)/2))+int(i*(len(list2)/2))])
    return FS

def update_stats(idteams,stats,ids):
    idt=dict()
    #Takes teams and the ladder and will update the stats for the next season.
    #Teams get bonus and penalities for the positions on the ladder.
    #First gets 8, last gets -7
    ranking_p = sorted(stats.iteritems(), sorttuples)
    for j in ids:
        idt[j]=np.array(idteams[j])
    #Top 5 score update
    idt[ranking_p[0][0]][1]=int(float(idt[ranking_p[0][0]][1]))+5
    idt[ranking_p[0][0]][2]=int(float(idt[ranking_p[0][0]][2]))+5
    idt[ranking_p[1][0]][1]=int(float(idt[ranking_p[1][0]][1]))+4
    idt[ranking_p[1][0]][2]=int(float(idt[ranking_p[1][0]][2]))+4
    idt[ranking_p[2][0]][1]=int(float(idt[ranking_p[2][0]][1]))+3
    idt[ranking_p[2][0]][2]=int(float(idt[ranking_p[2][0]][2]))+3
    idt[ranking_p[3][0]][1]=int(float(idt[ranking_p[3][0]][1]))+2
    idt[ranking_p[3][0]][2]=int(float(idt[ranking_p[3][0]][2]))+2
    idt[ranking_p[4][0]][1]=int(float(idt[ranking_p[4][0]][1]))+1
    idt[ranking_p[4][0]][2]=int(float(idt[ranking_p[4][0]][2]))+1
    #Bottom 5 score update
    idt[ranking_p[15][0]][1]=int(float(idt[ranking_p[15][0]][1]))-1
    idt[ranking_p[15][0]][2]=int(float(idt[ranking_p[15][0]][2]))-1
    idt[ranking_p[16][0]][1]=int(float(idt[ranking_p[16][0]][1]))-2
    idt[ranking_p[16][0]][2]=int(float(idt[ranking_p[16][0]][2]))-2
    idt[ranking_p[17][0]][1]=int(float(idt[ranking_p[17][0]][1]))-3
    idt[ranking_p[17][0]][2]=int(float(idt[ranking_p[17][0]][2]))-3
    idt[ranking_p[18][0]][1]=int(float(idt[ranking_p[18][0]][1]))-4
    idt[ranking_p[18][0]][2]=int(float(idt[ranking_p[18][0]][2]))-4
    idt[ranking_p[19][0]][1]=int(float(idt[ranking_p[19][0]][1]))-5
    idt[ranking_p[19][0]][2]=int(float(idt[ranking_p[19][0]][2]))-5
    if int(float(idt[ranking_p[15][0]][1]))< 1:
        idt[ranking_p[15][0]][1]=1
    if int(float(idt[ranking_p[16][0]][1]))< 1:
        idt[ranking_p[16][0]][1]=1
    if int(float(idt[ranking_p[17][0]][1]))< 1:
        idt[ranking_p[17][0]][1]=1
    if int(float(idt[ranking_p[18][0]][1]))< 1:
        idt[ranking_p[18][0]][1]=1
    if int(float(idt[ranking_p[19][0]][1]))< 1:
        idt[ranking_p[19][0]][1]=1
    if int(float(idt[ranking_p[15][0]][2]))< 1:
        idt[ranking_p[15][0]][2]=1
    if int(float(idt[ranking_p[16][0]][2]))< 1:
        idt[ranking_p[16][0]][2]=1
    if int(float(idt[ranking_p[17][0]][2]))< 1:
        idt[ranking_p[17][0]][2]=1
    if int(float(idt[ranking_p[18][0]][2]))< 1:
        idt[ranking_p[18][0]][2]=1
    if int(float(idt[ranking_p[19][0]][2]))< 1:
        idt[ranking_p[19][0]][2]=1
    return idt