#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 21:34:30 2022

@author: pete
"""

import numpy as np  
from premierleague_fncs import *
import re   
from functools import reduce
import functools
import _pickle as cpk
import math
"""
fopen=open("/Users/pete/Documents/Software/EPL/DIV1.pickle",'rb')
div1=cpk.load(fopen)
fopen.close()

fopen=open("/Users/pete/Documents/Software/EPL/prem.pickle",'rb')
prem=cpk.load(fopen)
fopen.close()

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 
    
"""

teams_full = [("Middlesborough",10,9,"MDL",9.5),
("Sunderland",9,10,"SUN",9.5),
("Crystal Palace",10,8,"CPL",9),
("Manchester United",10,8,"MNU",9),
("Charlton",8,10,"CHA",9),
("Leeds",8,10,"LDS",9),
("Liverpool",8,9,"LIV",8.5),
("Swansea",8,9,"SWA",8.5),
("Cardiff",9,8,"CAR",8.5),
("Chelsea",10,5,"CHE",7.5),
("Leciester City",10,5,"LEC",7.5),
("AFC Bournmouth",5,10,"BOU",7.5),
("Manchester City",5,10,"MNC",7.5),
("Barnsley",6,9,"BAR",7.5),
("Notts County",8,7,"NOC",7.5),
("West Brom",7,8,"WBA",7.5),
("AFC Wimbledon",9,5,"WIM",7),
("Arsenal",9,5,"ARS",7),
("Bolton",7,7,"BOL",7),
("Fulham",7,7,"FUL",7),
("Blackburn Rovers",7,7,"BBR",7),
("Bristol Rovers",7,7,"BRO",7),
("Derby",4,10,"DER",7),
("Nottingham Forest",9,4,"NOT",6.5),
("Bristol City",7,5,"BCI",6),
("Everton",7,5,"EVE",6),
("Blackpool",5,7,"BPL",6),
("Tottenham",6,5,"TOT",5.5),
("West Ham",6,5,"WHU",5.5),
("Coventry",1,10,"COV",5.5),
("Aston Villa",6,4,"ATV",5),
("Newcastle",6,4,"NEW",5),
("Norwich",5,5,"NOR",5),
("Brighton",7,2,"BHA",4.5),
("Ipswich",1,8,"IPT",4.5),
("Queens Park",5,4,"QPR",4.5),
("Birmingham City",2,6,"BIC",4),
("Burnley",6,2,"BUR",4),
("Luton",0,8,"LUT",4),
("Hull",4,3,"HUL",3.5),
("Wigan",4,3,"WIG",3.5),
("Oldham",7,0,"OLD",3.5),
("Milwall",2,1,"MIL",1.5),
("Brentford",0,0,"BRE",0)]





fopen=open("/Users/petekuzma/Documents/Software/EPL/TEAM_LIST.pickle",'wb')
cpk.dump(teams_full,fopen)
fopen.close()

fopen=open("/Users/petekuzma/Documents/Software/EPL/TEAM_LIST_orig.pickle",'wb')
cpk.dump(teams_full,fopen)
fopen.close()

fopen=open("/Users/pete/Documents/Software/EPL/TEAM_LIST_orig.pickle",'rb')
#fopen=open("/Users/petekuzma/Documents/Software/EPL/TEAM_LIST.pickle",'rb')
teams_full=cpk.load(fopen)
fopen.close()

ids=[]
id2team=dict()
for i in range(len(teams_full)):
    ids.append(teams_full[i][3])
    id2team[teams_full[i][3]]=teams_full[i][0:5]
    
import os
import shutil
fdir="/Users/petekuzma/Documents/Software/EPL/TEAM_STATS.pickle"
Pdir="/Users/petekuzma/Documents/Software/EPL/TEAM_PREM_STATS.pickle"
Ddir="/Users/petekuzma/Documents/Software/EPL/TEAM_DIV1_STATS.pickle"

FULLDICT=dict()
if os.path.isfile("TEAM_STATS.pickle") !=True:
    for i in ids:
        FULLDICT[i]=dict()
        FULLDICT[i]['POS_PREM']=[]
        FULLDICT[i]['POS_DIV1']=[]
        FULLDICT[i]['POS_ALTM']=[]
        FULLDICT[i]['M']=[]
        FULLDICT[i]['W']=[]
        FULLDICT[i]['D']=[]
        FULLDICT[i]['L']=[]
        FULLDICT[i]['Gs']=[]
        FULLDICT[i]['Gr']=[]
        FULLDICT[i]['P']=[]
        FULLDICT[i]['HM']=[]
        FULLDICT[i]['HW']=[]
        FULLDICT[i]['HD']=[]
        FULLDICT[i]['HL']=[]
        FULLDICT[i]['HGs']=[]
        FULLDICT[i]['HGr']=[]
        FULLDICT[i]['HP']=[]
        FULLDICT[i]['AM']=[]
        FULLDICT[i]['AW']=[]
        FULLDICT[i]['AD']=[]
        FULLDICT[i]['AL']=[]
        FULLDICT[i]['AGs']=[]
        FULLDICT[i]['AGr']=[]
        FULLDICT[i]['AP']=[]
        FULLDICT[i]['HSTR']=[]
        FULLDICT[i]['ASTR']=[]
        FULLDICT[i]['X_STR']=[]
    fopen=open(fdir,'wb')
    cpk.dump(FULLDICT,fopen)
    fopen.close()
    shutil.copyfile(fdir,Pdir)
    shutil.copyfile(fdir,Ddir)
else:
    print("Initialised")

print("Updating prem stats")
fopen=open(Pdir,'rb')
FULLDICT=cpk.load(fopen)
fopen.close()


for i in range(len(prem)):
    FULLDICT[prem[i][0]]['POS_PREM'].append(i+1)
    FULLDICT[prem[i][0]]['M'].append(prem[i][1][0])
    FULLDICT[prem[i][0]]['W'].append(prem[i][1][1])
    FULLDICT[prem[i][0]]['D'].append(prem[i][1][2])
    FULLDICT[prem[i][0]]['L'].append(prem[i][1][3])
    FULLDICT[prem[i][0]]['Gs'].append(prem[i][1][4])
    FULLDICT[prem[i][0]]['Gr'].append(prem[i][1][5])
    FULLDICT[prem[i][0]]['P'].append(prem[i][1][6])
    FULLDICT[prem[i][0]]['HM'].append(prem[i][1][7])
    FULLDICT[prem[i][0]]['HW'].append(prem[i][1][8])
    FULLDICT[prem[i][0]]['HD'].append(prem[i][1][9])
    FULLDICT[prem[i][0]]['HL'].append(prem[i][1][10])
    FULLDICT[prem[i][0]]['HGs'].append(prem[i][1][11])
    FULLDICT[prem[i][0]]['HGr'].append(prem[i][1][12])
    FULLDICT[prem[i][0]]['HP'].append(prem[i][1][13])
    FULLDICT[prem[i][0]]['AM'].append(prem[i][1][14])
    FULLDICT[prem[i][0]]['AW'].append(prem[i][1][15])
    FULLDICT[prem[i][0]]['AD'].append(prem[i][1][16])
    FULLDICT[prem[i][0]]['AL'].append(prem[i][1][17])
    FULLDICT[prem[i][0]]['AGs'].append(prem[i][1][18])
    FULLDICT[prem[i][0]]['AGr'].append(prem[i][1][19])
    FULLDICT[prem[i][0]]['AP'].append(prem[i][1][20])
    FULLDICT[prem[i][0]]['HSTR'].append(id2team[prem[i][0]][1])
    FULLDICT[prem[i][0]]['ASTR'].append(id2team[prem[i][0]][2])
    FULLDICT[prem[i][0]]['X_STR'].append(id2team[prem[i][0]][4])
    team=prem[i][0]
    if i==0:
        ids_prem=np.copy(ids)
        ids_prem=ids_prem[ids_prem!=team]
    else:
        ids_prem=ids_prem[ids_prem!=team]

for i in range(len(ids_prem)):
    FULLDICT[ids_prem[i]]['POS_PREM'].append(np.nan)
    FULLDICT[ids_prem[i]]['M'].append(np.nan)
    FULLDICT[ids_prem[i]]['W'].append(np.nan)
    FULLDICT[ids_prem[i]]['D'].append(np.nan)
    FULLDICT[ids_prem[i]]['L'].append(np.nan)
    FULLDICT[ids_prem[i]]['Gs'].append(np.nan)
    FULLDICT[ids_prem[i]]['Gr'].append(np.nan)
    FULLDICT[ids_prem[i]]['P'].append(np.nan)
    FULLDICT[ids_prem[i]]['HM'].append(np.nan)
    FULLDICT[ids_prem[i]]['HW'].append(np.nan)
    FULLDICT[ids_prem[i]]['HD'].append(np.nan)
    FULLDICT[ids_prem[i]]['HL'].append(np.nan)
    FULLDICT[ids_prem[i]]['HGs'].append(np.nan)
    FULLDICT[ids_prem[i]]['HGr'].append(np.nan)
    FULLDICT[ids_prem[i]]['HP'].append(np.nan)
    FULLDICT[ids_prem[i]]['AM'].append(np.nan)
    FULLDICT[ids_prem[i]]['AW'].append(np.nan)
    FULLDICT[ids_prem[i]]['AD'].append(np.nan)
    FULLDICT[ids_prem[i]]['AL'].append(np.nan)
    FULLDICT[ids_prem[i]]['AGs'].append(np.nan)
    FULLDICT[ids_prem[i]]['AGr'].append(np.nan)
    FULLDICT[ids_prem[i]]['AP'].append(np.nan)
    FULLDICT[ids_prem[i]]['HSTR'].append(np.nan)
    FULLDICT[ids_prem[i]]['ASTR'].append(np.nan)
    FULLDICT[ids_prem[i]]['X_STR'].append(np.nan)

fopen=open(Pdir,'wb')
cpk.dump(FULLDICT,fopen)
fopen.close()


print("Updating Div1 stats")
fopen=open(Ddir,'rb')
FULLDICT=cpk.load(fopen)
fopen.close()


for i in range(len(div1)):
    FULLDICT[div1[i][0]]['POS_DIV1'].append(i+1)
    FULLDICT[div1[i][0]]['M'].append(div1[i][1][0])
    FULLDICT[div1[i][0]]['W'].append(div1[i][1][1])
    FULLDICT[div1[i][0]]['D'].append(div1[i][1][2])
    FULLDICT[div1[i][0]]['L'].append(div1[i][1][3])
    FULLDICT[div1[i][0]]['Gs'].append(div1[i][1][4])
    FULLDICT[div1[i][0]]['Gr'].append(div1[i][1][5])
    FULLDICT[div1[i][0]]['P'].append(div1[i][1][6])
    FULLDICT[div1[i][0]]['HM'].append(div1[i][1][7])
    FULLDICT[div1[i][0]]['HW'].append(div1[i][1][8])
    FULLDICT[div1[i][0]]['HD'].append(div1[i][1][9])
    FULLDICT[div1[i][0]]['HL'].append(div1[i][1][10])
    FULLDICT[div1[i][0]]['HGs'].append(div1[i][1][11])
    FULLDICT[div1[i][0]]['HGr'].append(div1[i][1][12])
    FULLDICT[div1[i][0]]['HP'].append(div1[i][1][13])
    FULLDICT[div1[i][0]]['AM'].append(div1[i][1][14])
    FULLDICT[div1[i][0]]['AW'].append(div1[i][1][15])
    FULLDICT[div1[i][0]]['AD'].append(div1[i][1][16])
    FULLDICT[div1[i][0]]['AL'].append(div1[i][1][17])
    FULLDICT[div1[i][0]]['AGs'].append(div1[i][1][18])
    FULLDICT[div1[i][0]]['AGr'].append(div1[i][1][19])
    FULLDICT[div1[i][0]]['AP'].append(div1[i][1][20])
    FULLDICT[div1[i][0]]['HSTR'].append(id2team[div1[i][0]][1])
    FULLDICT[div1[i][0]]['ASTR'].append(id2team[div1[i][0]][2])
    FULLDICT[div1[i][0]]['X_STR'].append(id2team[div1[i][0]][-1])
    team=div1[i][0]
    if i==0:
        ids_div1=np.copy(ids)
        ids_div1=ids_div1[ids_div1!=team]
    else:
        ids_div1=ids_div1[ids_div1!=team]

for i in range(len(ids_div1)):
    FULLDICT[ids_div1[i]]['POS_DIV1'].append(np.nan)
    FULLDICT[ids_div1[i]]['M'].append(np.nan)
    FULLDICT[ids_div1[i]]['W'].append(np.nan)
    FULLDICT[ids_div1[i]]['D'].append(np.nan)
    FULLDICT[ids_div1[i]]['L'].append(np.nan)
    FULLDICT[ids_div1[i]]['Gs'].append(np.nan)
    FULLDICT[ids_div1[i]]['Gr'].append(np.nan)
    FULLDICT[ids_div1[i]]['P'].append(np.nan)
    FULLDICT[ids_div1[i]]['HM'].append(np.nan)
    FULLDICT[ids_div1[i]]['HW'].append(np.nan)
    FULLDICT[ids_div1[i]]['HD'].append(np.nan)
    FULLDICT[ids_div1[i]]['HL'].append(np.nan)
    FULLDICT[ids_div1[i]]['HGs'].append(np.nan)
    FULLDICT[ids_div1[i]]['HGr'].append(np.nan)
    FULLDICT[ids_div1[i]]['HP'].append(np.nan)
    FULLDICT[ids_div1[i]]['AM'].append(np.nan)
    FULLDICT[ids_div1[i]]['AW'].append(np.nan)
    FULLDICT[ids_div1[i]]['AD'].append(np.nan)
    FULLDICT[ids_div1[i]]['AL'].append(np.nan)
    FULLDICT[ids_div1[i]]['AGs'].append(np.nan)
    FULLDICT[ids_div1[i]]['AGr'].append(np.nan)
    FULLDICT[ids_div1[i]]['AP'].append(np.nan)
    FULLDICT[ids_div1[i]]['HSTR'].append(np.nan)
    FULLDICT[ids_div1[i]]['ASTR'].append(np.nan)
    FULLDICT[ids_div1[i]]['X_STR'].append(np.nan)


fopen=open(Ddir,'wb')
cpk.dump(FULLDICT,fopen)
fopen.close()

print("Updating all-time stats")
ENTIRE=prem+div1
fopen=open(fdir,'rb')
FULLDICT=cpk.load(fopen)
fopen.close()

for i in range(len(ENTIRE)):
    FULLDICT[ENTIRE[i][0]]['POS_ALTM'].append(i+1)
    FULLDICT[ENTIRE[i][0]]['M'].append(ENTIRE[i][1][0])
    FULLDICT[ENTIRE[i][0]]['W'].append(ENTIRE[i][1][1])
    FULLDICT[ENTIRE[i][0]]['D'].append(ENTIRE[i][1][2])
    FULLDICT[ENTIRE[i][0]]['L'].append(ENTIRE[i][1][3])
    FULLDICT[ENTIRE[i][0]]['Gs'].append(ENTIRE[i][1][4])
    FULLDICT[ENTIRE[i][0]]['Gr'].append(ENTIRE[i][1][5])
    FULLDICT[ENTIRE[i][0]]['P'].append(ENTIRE[i][1][6])
    FULLDICT[ENTIRE[i][0]]['HM'].append(ENTIRE[i][1][7])
    FULLDICT[ENTIRE[i][0]]['HW'].append(ENTIRE[i][1][8])
    FULLDICT[ENTIRE[i][0]]['HD'].append(ENTIRE[i][1][9])
    FULLDICT[ENTIRE[i][0]]['HL'].append(ENTIRE[i][1][10])
    FULLDICT[ENTIRE[i][0]]['HGs'].append(ENTIRE[i][1][11])
    FULLDICT[ENTIRE[i][0]]['HGr'].append(ENTIRE[i][1][12])
    FULLDICT[ENTIRE[i][0]]['HP'].append(ENTIRE[i][1][13])
    FULLDICT[ENTIRE[i][0]]['AM'].append(ENTIRE[i][1][14])
    FULLDICT[ENTIRE[i][0]]['AW'].append(ENTIRE[i][1][15])
    FULLDICT[ENTIRE[i][0]]['AD'].append(ENTIRE[i][1][16])
    FULLDICT[ENTIRE[i][0]]['AL'].append(ENTIRE[i][1][17])
    FULLDICT[ENTIRE[i][0]]['AGs'].append(ENTIRE[i][1][18])
    FULLDICT[ENTIRE[i][0]]['AGr'].append(ENTIRE[i][1][19])
    FULLDICT[ENTIRE[i][0]]['AP'].append(ENTIRE[i][1][20])
    FULLDICT[ENTIRE[i][0]]['HSTR'].append(id2team[ENTIRE[i][0]][1])
    FULLDICT[ENTIRE[i][0]]['ASTR'].append(id2team[ENTIRE[i][0]][2])
    FULLDICT[ENTIRE[i][0]]['X_STR'].append(id2team[ENTIRE[i][0]][-1])

fopen=open(fdir,'wb')
cpk.dump(FULLDICT,fopen)
fopen.close()

print("updated all scores")
print("Creating next seasons team lists and updated statistics..")

teamarray=np.array(teams_full)
for i in range(len(teamarray)):
    #print(i)
    pos_str=i
    team_short=teams_full[i][3]
    l=0
    match="no"
    while match=="no":
        en_team_short=ENTIRE[l][0]
        if en_team_short==team_short:
            pos=l
            match="yes"
        else:
            l+=1
    diff_str = (pos_str-pos)
    if i == 20:
        print("-------------------")
    print("team: {0}, expected: {1}, actual: {2}".format(teams_full[i][0],pos_str+1,pos+1))
    if 10 >= diff_str >=5:
        teamarray[i][1]=str(math.ceil(int(teamarray[i][1])*1.025))
        teamarray[i][2]=str(math.ceil(int(teamarray[i][2])*1.025))
        if int(teamarray[i][1])==0:
            teamarray[i][1]=str(1)
        if int(teamarray[i][2])==0:
            teamarray[i][2]=str(1)
        teamarray[i][4]=float((int(teamarray[i][1])+int(teamarray[i][2]))/2.)
    elif diff_str >=10:
        teamarray[i][1]=str(math.ceil(int(teamarray[i][1])*1.05))
        teamarray[i][2]=str(math.ceil(int(teamarray[i][2])*1.05))
        if int(teamarray[i][1])==0:
            teamarray[i][1]=str(1)
        if int(teamarray[i][2])==0:
            teamarray[i][2]=str(1)
        teamarray[i][4]=float((int(teamarray[i][1])+int(teamarray[i][2]))/2.)
    elif -10 <= diff_str<=-5:
        teamarray[i][1]=str(math.floor(int(teamarray[i][1])/1.025))
        teamarray[i][2]=str(math.floor(int(teamarray[i][2])/1.025))
        if int(teamarray[i][1])==1:
            teamarray[i][1]=str(0)
        if int(teamarray[i][2])==1:
            teamarray[i][2]=str(0)
        teamarray[i][4]=(int(teamarray[i][1])+int(teamarray[i][2]))/2.
    elif diff_str<=-10:
        teamarray[i][1]=str(math.floor(int(teamarray[i][1])/1.05))
        teamarray[i][2]=str(math.floor(int(teamarray[i][2])/1.05))
        if int(teamarray[i][1])==1:
            teamarray[i][1]=str(0)
        if int(teamarray[i][2])==1:
            teamarray[i][2]=str(0)
        teamarray[i][4]=(int(teamarray[i][1])+int(teamarray[i][2]))/2.
    else:
        pass


teamrrf=[]
for i in range(len(teamarray)):
    entry=(teamarray[i][0],int(teamarray[i][1]),int(teamarray[i][2]),\
    teamarray[i][3],float(teamarray[i][4]))
    teamrrf.append(entry)
teams_full=sorted(teamrrf,key=lambda x:x[4],reverse=True)

fopen=open("/Users/pete/Documents/Software/EPL/TEAM_LIST.pickle",'wb')
cpk.dump(teams_full,fopen)
fopen.close()


premlist=[]
pids=np.copy(teams_full)
for i in range(20):
    if i in (16,17,18,19):
        pds=pids[pids[:,0]==id2team[div1[i-16][0]][0]]
        premlist.append((pds[0][0]+" (*)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==0:
        pds=pids[pids[:,0]==id2team[prem[i][0]][0]]
        premlist.append((pds[0][0]+" (1)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==1:
        pds=pids[pids[:,0]==id2team[prem[i][0]][0]]
        premlist.append((pds[0][0]+" (2)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==2:
        pds=pids[pids[:,0]==id2team[prem[i][0]][0]]
        premlist.append((pds[0][0]+" (3)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==3:
        pds=pids[pids[:,0]==id2team[prem[i][0]][0]]
        premlist.append((pds[0][0]+" (4)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    else:
        pds=pids[pids[:,0]==id2team[prem[i][0]][0]]
        premlist.append((pds[0][0],int(pds[0][1]),int(pds[0][2]),pds[0][3]))
 
fopen=open("/Users/pete/Documents/Software/EPL/premlist.pickle",'wb')
cpk.dump(premlist,fopen)
fopen.close()

div1list=[]
pids=np.copy(teams_full)
for i in range(24):
    if i in (0,1,2,3):
        pds=pids[pids[:,0]==id2team[prem[i+16][0]][0]]
        div1list.append((pds[0][0]+" (*)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==4:
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        #print(pds)
        div1list.append((pds[0][0]+" (5)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==5:
        #print(pds)
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        div1list.append((pds[0][0]+" (6)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==6:
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        div1list.append((pds[0][0]+" (7)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==23:
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        #print(pds)
        div1list.append((pds[0][0]+" (24)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==22:
        #print(pds)
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        div1list.append((pds[0][0]+" (23)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==21:
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        div1list.append((pds[0][0]+" (22)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==20:
        #print(pds)
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        div1list.append((pds[0][0]+" (21)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    elif i==19:
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        div1list.append((pds[0][0]+" (20)",int(pds[0][1]),int(pds[0][2]),pds[0][3]))
    else:
        pds=pids[pids[:,0]==id2team[div1[i][0]][0]]
        div1list.append((pds[0][0],int(pds[0][1]),int(pds[0][2]),pds[0][3]))

 
fopen=open("/Users/pete/Documents/Software/EPL/div1list.pickle",'wb')
cpk.dump(div1list,fopen)
fopen.close()

'''
#-----
fopen=open("/Users/pete/Documents/Software/EPL/TEAM_LIST.pickle",'rb')
f1=cpk.load(fopen)
fopen.close()

fopen=open("/Users/pete/Documents/Software/EPL/TEAM_LIST_orig.pickle",'rb')
f2=cpk.load(fopen)
fopen.close()
for i in range(len(f1))
#----
'''