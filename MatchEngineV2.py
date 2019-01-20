#Import randomize function
from random import randint

#Generate HOME team
home_info={'name':'CSKA'}
home=[{'num':35,'fam':'Akinfeev','pos':'GK','gk':70,'def':15,'mid':0,'att':0,'name':'CSKA'}]
home.append({'num':14,'fam':'Nababkin','pos':'DEF','gk':0,'def':60,'mid':30,'att':10})
home.append({'num':50,'fam':'Becao','pos':'DEF','gk':0,'def':55,'mid':10,'att':5})
home.append({'num':23,'fam':'Magnusson','pos':'DEF','gk':0,'def':75,'mid':20,'att':10})
home.append({'num':2,'fam':'Fernandes','pos':'MID','gk':0,'def':25,'mid':80,'att':45})
home.append({'num':77,'fam':'Akhmetov','pos':'MID','gk':0,'def':5,'mid':65,'att':45})
home.append({'num':25,'fam':'Bistrovic','pos':'MID','gk':0,'def':10,'mid':70,'att':40})
home.append({'num':8,'fam':'Vlasic','pos':'MID','gk':0,'def':5,'mid':75,'att':30})
home.append({'num':15,'fam':'Efremov','pos':'MID','gk':0,'def':15,'mid':60,'att':25})
home.append({'num':11,'fam':'Hernandez','pos':'ATT','gk':0,'def':3,'mid':40,'att':90})
home.append({'num':9,'fam':'Chalov','pos':'ATT','gk':0,'def':8,'mid':23,'att':70})

#Generate AWAY team
away_info={'name':'URAL'}
away=[{'num':31,'fam':'Godzyur','pos':'GK','gk':60,'def':25,'mid':0,'att':0,'name':'URAL'}]
away.append({'num':27,'fam':'Merkulov','pos':'DEF','gk':0,'def':40,'mid':25,'att':15})
away.append({'num':6,'fam':'Balazic','pos':'DEF','gk':0,'def':60,'mid':10,'att':15})
away.append({'num':4,'fam':'Bryzgalov','pos':'DEF','gk':0,'def':55,'mid':10,'att':10})
away.append({'num':15,'fam':'Kulakov','pos':'DEF','gk':0,'def':50,'mid':5,'att':15})
away.append({'num':70,'fam':'Zhigulev','pos':'MID','gk':0,'def':20,'mid':55,'att':40})
away.append({'num':13,'fam':'Boumal','pos':'MID','gk':0,'def':10,'mid':50,'att':40})
away.append({'num':58,'fam':'El Kabir','pos':'MID','gk':0,'def':10,'mid':60,'att':30})
away.append({'num':10,'fam':'Bicfalvi','pos':'MID','gk':0,'def':5,'mid':70,'att':35})
away.append({'num':17,'fam':'Dimitrov','pos':'MID','gk':0,'def':5,'mid':45,'att':15})
away.append({'num':20,'fam':'Panyukov','pos':'ATT','gk':0,'def':3,'mid':35,'att':70})

#Function that calculates team streight while control in attack zone
def attack_streight(team):
    att=0
    for player in team:
        if player['pos']=='ATT':
            att+=player['att']
        elif player['pos']=='MID':
            att+=0.4*player['att']
        elif player['pos']=='DEF':
            att+=0.2*player['att']
    return int(att)
#Function that calculates team streight while defense or control in defense zone
def defense_streight(team):
    dfn=0
    for player in team:
        if player['pos']=='ATT':
            dfn+=0.2*player['def']
        elif player['pos']=='MID':
            dfn+=0.4*player['def']
        elif player['pos']=='DEF':
            dfn+=player['def']
    return int(dfn)
#Function that calculates team streight while control in midfield zone
def midfield_streight(team):
    mid=0
    for player in team:
        if player['pos']=='ATT':
            mid+=0.4*player['mid']
        elif player['pos']=='MID':
            mid+=player['mid']
        elif player['pos']=='DEF':
            mid+=0.4*player['mid']
    return int(mid)
#Function that calculates team streight while defense in midfield zone
def midfield_def_streight(team):
    middef=0
    for player in team:
        if player['pos']=='ATT':
            middef+=0.4*player['def']
        elif player['pos']=='MID':
            middef+=player['def']
        elif player['pos']=='DEF':
            middef+=0.4*player['def']
    return int(middef)
#Function that calculates team streight while defense in attack zone
def attack_def_streight(team):
    attdef=0
    for player in team:
        if player['pos']=='ATT':
            attdef+=player['def']
        elif player['pos']=='MID':
            attdef+=0.4*player['def']
        elif player['pos']=='DEF':
            attdef+=0.2*player['def']
    return int(attdef)

#Function that calculates active player
def choose_player(team,position,action):
    rating_table=[]
    rating=0
    for player in team:
        if player['pos']=='GK':
            continue
        if position=='defense':
            if player['pos']=='DEF':
                rating+=player['def']
            elif player['pos']=='MID':
                rating+=0.3*player['def']
            elif player['pos']=='ATT':
                rating+=0.1*player['def']
        elif position=='midfield' and action=='control':
            if player['pos']=='DEF':
                rating+=0.3*player['mid']
            elif player['pos']=='MID':
                rating+=player['mid']
            elif player['pos']=='ATT':
                rating+=0.3*player['mid']
        elif position=='midfield' and action=='pressing':
            if player['pos']=='DEF':
                rating+=0.3*player['def']
            elif player['pos']=='MID':
                rating+=player['def']
            elif player['pos']=='ATT':
                rating+=0.3*player['def']
        elif position=='attack' and action=='control':
            if player['pos']=='DEF':
                rating+=0.1*player['att']
            elif player['pos']=='MID':
                rating+=0.3*player['att']
            elif player['pos']=='ATT':
                rating+=player['att']
        elif position=='attack' and action=='pressing':
            if player['pos']=='DEF':
                rating+=0.1*player['def']
            elif player['pos']=='MID':
                rating+=0.3*player['def']
            elif player['pos']=='ATT':
                rating+=player['def']
        rating_table.append([player,int(rating)])
    player_roll=randint(0,int(rating))
    for player_stat in rating_table:
        if player_stat[1]>=player_roll:
            active_player=player_stat[0]
            break
    return active_player

def match_init():
    h_score=0
    a_score=0
    b_pos='midfield'
    if randint(0,1)==0:
        cont=0
        c_team=home
        op_team=away
        print(c_team[0]['name']+' will start the game')
    else:
        cont=1
        c_team=away
        op_team=home
        print(c_team[0]['name']+' will start the game')
    a_player=choose_player(c_team,'midfield','control')
    return h_score,a_score,b_pos,cont, c_team, op_team, a_player

def match_action(h_score,a_score,b_pos, c_team, op_team,a_player):
    #Processing match situation in midfield zone
    if b_pos=='midfield':
            defense=midfield_def_streight(op_team)
            attack=midfield_streight(c_team)
            print(c_team[0]['name']+' has control')
            print(a_player['fam']+' with the ball')
        roll=randint(0,defense+attack)
        print('The Roll is '+str(roll)+'(0-'+str(defense//2)+' - Loose ball,'+str(defense//2)+'-'+str(defense)+' - Pass back,'+str(defense)+'-'+str(defense+attack//2)+' - Keep Control,'+str(defense+attack//2)+'-'+str(defense+attack)+' - Pass Forward)')
        if roll<=defense//2:
            print(op_team[0]['name']+' team takes the ball')
            t_team=op_team
            op_team=c_team
            c_team=t_team
            a_player=choose_player(c_team,'midfield','pressing')
            print(a_player['fam']+' takes the ball')      
        elif roll<=defense:
            print(c_team[0]['name']+' needs to Pass back. Ball goes to '+c_team[0]['name']+"'s zone")
            if c_team=home:
                b_pos='homezone'
            else:
                b_pos='awayzone'
            c_player=a_player
            while c_player==a_player:
                a_player=c_player(c_team,'defense','control')
            print('Ball goes back to '+a_player['fam'])
        elif roll<=defense+attack//2:
            print(c_team[0]['name']+' holds the ball in the midfield zone')
            c_player=a_player
            a_player=choose_player(c_team,'midfield','control')
            if a_player!=c_player:
                print('Ball goes to '+a_player['fam'])
            else:
                print(a_player['fam']+' keeps the ball')
        elif roll<=defense+attack:
            print(c_team[0]['name']+' passes the ball forward. Ball goes to '+op_team[0]['name']+"'s zone")
            if c_team=home:
                b_pos="awayzone"
            else
                b_pos="homezone"
            c_player=a_player
            while c_player=a_player:
                a_player=choose_player(c_team,'attack','control')
            print('Ball goes forward to '+a_player['fam'])
#Processing match situation in homezone zone
    elif b_pos=='homezone':
        if c_team==home:
            defense=attack_def_streight(op_team)
            attack=defense_streight(c_team)  
        else:
            defense=defense_streight(op_team)
            attack=attack_streight(c_team)
        print(c_team[0]['name']+" has control")
        print(a_player['fam']+' with the ball')
        roll=randint(0,defense+attack)
        if c_team==home:
           print('The Roll is '+str(roll)+'(0-'+str(defense//2)+' - Loose ball,'+str(defense//2)+'-'+str(defense)+' - Pass back,'+str(defense)+'-'+str(defense+attack//2)+' - Keep Control,'+str(defense+attack//2)+'-'+str(defense+attack)+' - Goal Chance)')
        else:
            print('The Roll is '+str(roll)+'(0-'+str(defense//2)+' - Loose ball,'+str(defense//2)+'-'+str(defense)+' - Pass back,'+str(defense)+'-'+str(defense+attack//2)+' - Keep Control,'+str(defense+attack//2)+'-'+str(defense+attack)+' - Pass Forward)')
        if roll<=defense//2: 
            if c_team==home:
                print("Great pressing! "+op_team[0]['name']+" team takes the ball near opposite's goals")
                a_player=choose_player(op_team,'attack','pressing')
            else:
                print("Great defending! "+op_team[0]['name']+" team takes the ball from attaker")
                a_player=choose_player(op_team,'defense','pressing')
            t_team=op_team
            op_team=c_team
            c_team=t_team
            print(a_player['fam']+' takes the ball')
        elif roll<=defense:
            if c_team==home:
                print("Hard pressing! "+c_team[0]['name']+"'s defenders need to pass back to their goalkeeper")
                a_player=home[0]
                b_pos='homebox'
                print(a_player['fam']+' takes the pass')
            else:
                print("Hard defending! "+c_team[0]['name']+"'s attakers need to pass back to midfield zone")
                ball="midfield"
                c_player=a_player
                while c_player==a_player:
                a_player=choose_player(c_team,'midfield','control')
                print('Ball goes back to '+a_player['fam'])
        elif roll<=defense+attack//2:
            if c_team==home:
                print(c_team[0]['name']+' still handle the ball near their goals')
                c_player=a_player
                a_player=choose_player(c_team,'defense','control')
                if a_player!=c_player:
                    print('Ball goes to '+a_player['fam'])
                else:
                    print(a_player['fam']+' keeps the ball')
            else:
                print("It is not over for now! "+c_team[0]['name']+"'s attakers still handle the ball")
                c_player=a_player
                a_player=choose_player(c_team,'attack','control')
                if active_player!=current_player:
                    print('Ball goes to '+active_player['fam'])
                else:
                    print(a_player['fam']+' keeps the ball')
        elif roll<=defense+attack:
            if c_team==home
                print(c_team[0]['name']+' passes the ball forward. Ball goes to the midfield zone')
                ball="midfield"
                c_player=a_player
                while c_player==a_player:
                    a_player=choose_player(c_team,'midfield','control')
                print('Ball goes forward to '+a_player['fam'])
            else:
                print("It is a chance for "+c_team[0]['name']+"! They past throught defense")
                b_pos='homebox'
                a_player=choose_player(c_team,'attack','control')
                print('A goal chance for '+a_player['fam']+'!!!')
#Processing match situation in awayzone zone
    elif ball=='awayzone':
        if c_team==away:
            defense=attack_def_streight(op_team)
            attack=defense_streight(c_team)  
        else:
            defense=defense_streight(op_team)
            attack=attack_streight(c_team)
        print(c_team[0]['name']+" has control")
        print(a_player['fam']+' with the ball')
        roll=randint(0,defense+attack)
        if c_team==away:
           print('The Roll is '+str(roll)+'(0-'+str(defense//2)+' - Loose ball,'+str(defense//2)+'-'+str(defense)+' - Pass back,'+str(defense)+'-'+str(defense+attack//2)+' - Keep Control,'+str(defense+attack//2)+'-'+str(defense+attack)+' - Goal Chance)')
        else:
            print('The Roll is '+str(roll)+'(0-'+str(defense//2)+' - Loose ball,'+str(defense//2)+'-'+str(defense)+' - Pass back,'+str(defense)+'-'+str(defense+attack//2)+' - Keep Control,'+str(defense+attack//2)+'-'+str(defense+attack)+' - Pass Forward)')
        if roll<=defense//2: 
            if c_team==away:
                print("Great pressing! "+op_team[0]['name']+" team takes the ball near opposite's goals")
                a_player=choose_player(op_team,'attack','pressing')
            else:
                print("Great defending! "+op_team[0]['name']+" team takes the ball from attaker")
                a_player=choose_player(op_team,'defense','pressing')
            t_team=op_team
            op_team=c_team
            c_team=t_team
            print(a_player['fam']+' takes the ball')
        elif roll<=defense:
            if c_team==away:
                print("Hard pressing! "+c_team[0]['name']+"'s defenders need to pass back to their goalkeeper")
                a_player=away[0]
                b_pos='awaybox'
                print(a_player['fam']+' takes the pass')
            else:
                print("Hard defending! "+c_team[0]['name']+"'s attakers need to pass back to midfield zone")
                ball="midfield"
                c_player=a_player
                while c_player==a_player:
                a_player=choose_player(c_team,'midfield','control')
                print('Ball goes back to '+a_player['fam'])
        elif roll<=defense+attack//2:
            if c_team==away:
                print(c_team[0]['name']+' still handle the ball near their goals')
                c_player=a_player
                a_player=choose_player(c_team,'defense','control')
                if a_player!=c_player:
                    print('Ball goes to '+a_player['fam'])
                else:
                    print(a_player['fam']+' keeps the ball')
            else:
                print("It is not over for now! "+c_team[0]['name']+"'s attakers still handle the ball")
                c_player=a_player
                a_player=choose_player(c_team,'attack','control')
                if active_player!=current_player:
                    print('Ball goes to '+active_player['fam'])
                else:
                    print(a_player['fam']+' keeps the ball')
        elif roll<=defense+attack:
            if c_team==away
                print(c_team[0]['name']+' passes the ball forward. Ball goes to the midfield zone')
                ball="midfield"
                c_player=a_player
                while c_player==a_player:
                    a_player=choose_player(c_team,'midfield','control')
                print('Ball goes forward to '+a_player['fam'])
            else:
                print("It is a chance for "+c_team[0]['name']+"! They past throught defense")
                b_pos='awaybox'
                a_player=choose_player(c_team,'attack','control')
                print('A goal chance for '+a_player['fam']+'!!!')
    return h_score,a_score,b_pos,c_team,a_player
            
print(home_info['name']+' defense streight is '+str(defense_streight(home)))
print(home_info['name']+' midfield streight is '+str(midfield_streight(home)))
print(home_info['name']+' attack streight is '+str(attack_streight(home)))
print(home_info['name']+' defense in midfield streight is '+str(midfield_def_streight(home)))
print(home_info['name']+' defense in attack streight is '+str(attack_def_streight(home)))
print('-')
print(away_info['name']+' defense streight is '+str(defense_streight(away)))
print(away_info['name']+' midfield streight is '+str(midfield_streight(away)))
print(away_info['name']+' attack streight is '+str(attack_streight(away)))
print(away_info['name']+' defense in midfield streight is '+str(midfield_def_streight(away)))
print(away_info['name']+' defense in attack streight is '+str(attack_def_streight(away)))
print('****************************************************************')
    
#Initiate match
home_score, away_score, ball, control, team_with_ball, active_player=match_init()    
for time in range(181):
    print('There is '+str(time//2)+' minute of the match')
    print('The ball is in the '+ball)
    
#Processing match situation in homebox zone
    elif ball=='homebox':
         if control==0:
             if active_player['pos']=='GK':
                 print(home_info['name']+' goalkeeper with the ball')    
                 opp_player=choose_player(away,'attack','pressing')
                 roll=randint(0, active_player['gk']+opp_player['def'])
                 print('The Roll is '+str(roll)+'(0-'+str(opp_player['def'])+' - Loose ball,'+str(opp_player['def'])+'-'+str(active_player['gk']+opp_player['def'])+' - Pass Forward)')
                 if roll<=opp_player['def']:
                     print('And.....he loses the ball to the attackers')
                     control=1
                     active_player=opp_player
                     print('A goal chance for '+active_player['fam']+'!!!')  
                 else:
                     print('And he succesefully passes the ball to defenders')
                     ball='homezone'
                     active_player=choose_player(home,'defense','control')
                     print('Ball goes forward to '+active_player['fam'])
             else:
                 print(active_player['fam']+' with the ball')    
                 opp_player=choose_player(away,'attack','pressing')
                 roll=randint(0, active_player['gk']+opp_player['def'])
                 print('The Roll is '+str(roll)+'(0-'+str(opp_player['def'])+' - Loose ball,'+str(opp_player['def'])+'-'+str(active_player['gk']+opp_player['def'])+' - Pass Forward)')
                 if roll<=opp_player['def']:
                     print('And.....he loses the ball to the attackers')
                     control=1
                     active_player=opp_player
                     print('A goal chance for '+active_player['fam']+'!!!')  
                 else:
                     print('And he succesefully clears the ball to teammates')
                     ball='homezone'
                     active_player=choose_player(home,'defense','control')
                     print('Ball goes forward to '+active_player['fam'])
         else:
             print('He shoots!....')
             #Расчет диапазонов точности
             if active_player['att']<=90:
                 roll=randint(0,100)
                 print('The Roll is '+str(roll)+'(0-'+str(active_player['att'])+' - to the Goal,'+str(active_player['att'])+'-'+str(100)+' - Wide)')
             else:
                 roll=randint(0,active_player['att']+10)
                 print('The Roll is '+str(roll)+'(0-'+str(active_player['att'])+' - to the Goal,'+str(active_player['att'])+'-'+str(active_player['gk']+10)+' - Wide)')    
             if roll<=active_player['att']:
                 print('Ball flies to the goal....')
                 opp_player=home[0]
                 #Расчет вариантов при попадании в ворота   
                 roll=randint(0,opp_player['gk']+active_player['att'])
                 print('The Roll is '+str(roll)+'(0-'+str(opp_player['gk']//2)+' - Save,'+str(opp_player['gk']//2)+'-'+str(opp_player['gk'])+' - Turn Out,'+str(opp_player['gk'])+'-'+str(opp_player['gk']+active_player['att']//2)+' - Do not reach out,'+str(opp_player['gk']+active_player['att']//2)+'-'+str(opp_player['gk']+active_player['att'])+' - Goal)')    
                 if roll<=opp_player['gk']//2:
                     print('but '+opp_player['fam']+' saves it!')
                     control=0
                     ball='homezone'
                     print('He throw the ball to defenders')
                     active_player=choose_player(home,'defense','control')
                     print(active_player['fam']+'with the ball')
                 elif roll<=opp_player['gk']:
                     print(opp_player['fam']+' turn the ball out!')
                     #Расчет вариантов отскока мяча
                     roll=randint(0,opp_player['gk']+active_player['att'])
                     print('The Roll is '+str(roll)+'(0-'+str(opp_player['gk']//2)+' - Out of the box,'+str(opp_player['gk']//2)+'-'+str(opp_player['gk'])+' - Corner,'+str(opp_player['gk'])+'-'+str(opp_player['gk']+active_player['att']//2)+' - To the box,'+str(opp_player['gk']+active_player['att']//2)+'-'+str(opp_player['gk']+active_player['att'])+' - to the goal)')    
                     if roll<=opp_player['gk']//2:
                         print('Ball flies away from the box')
                         ball='homezone'
                         #Расчет подбора мяча
                         defense=defense_streight(home)
                         attack=attack_streight(away)
                         roll=randint(0,defense+attack)
                         print('The Roll is '+str(roll)+'(0-'+str(defense)+' - Defense,'+str(defense)+'-'+str(defense+attack)+' - Attack)')
                         if roll<=defense:
                             control=0
                             print('Defenders takes the ball')
                             active_player=choose_player(home,'defense','control')
                             print('Ball goes to '+active_player['fam'])
                         else:
                             control=1
                             print('Attack is not over. Attackers takes the ball')
                             active_player=choose_player(away,'attack','control')
                             print('Ball goes to '+active_player['fam'])
                     elif roll<=opp_player['gk']:
                         #ball='homecorner'
                         ball='homezone'
                         print('Ball goes to corner')
                         control=0
                         active_player=choose_player(home,'defense','control')
                         print('Ball goes to '+active_player['fam'])
                     elif roll<=opp_player['gk']+active_player['att']//2:
                         print('Ball flies to the box')
                         ball='homebox'
                         #Расчет подбора мяча
                         defense=defense_streight(home)
                         attack=attack_streight(away)
                         roll=randint(0,defense+attack)
                         print('The Roll is '+str(roll)+'(0-'+str(defense)+' - Defense,'+str(defense)+'-'+str(defense+attack)+' - Attack)')
                         if roll<=defense:
                             control=0
                             print('Defenders takes the ball')
                             active_player=choose_player(home,'defense','control')
                             print('Ball goes to '+active_player['fam'])
                         else:
                             control=1
                             print('Another chance. Attackers takes the ball')
                             active_player=choose_player(away,'attack','control')
                             print('Chance for '+active_player['fam'])
                     else:
                         print('But the ball falls to the goal by the hand of the goalkeeper')
                         away_score+=1
                         ball='midfield'
                         control=0
                         print('Score is '+str(home_score)+':'+str(away_score))
                         active_player=choose_player(home,'midfield','control')
                 elif roll<=opp_player['gk']+active_player['att']//2:
                     print(opp_player['fam']+' do not reach out the ball')
                     #Расчет вариантов, когда вратать обыгран
                     defense=defense_streight(home)
                     roll=randint(0,defense//4+active_player['att'])
                     print('The Roll is '+str(roll)+'(0-'+str(defense//12)+' - Out of the box,'+str(defense//12)+'-'+str(defense//6)+' - To the corner,'+str(defense//6)+'-'+str(defense//4)+' - To the box,'+str(defense//4)+'-'+str(defense//4+active_player['att'])+' - To the Goal)')
                     if roll<=defense/12:
                         print('But defender clears it out of the box')
                         ball='homezone'
                         #Расчет подбора мяча
                         defense=defense_streight(home)
                         attack=attack_streight(away)
                         roll=randint(0,defense+attack)
                         print('The Roll is '+str(roll)+'(0-'+str(defense)+' - Defense,'+str(defense)+'-'+str(defense+attack)+' - Attack)')
                         if roll<=defense:
                             control=0
                             print('Defenders takes the ball')
                             active_player=choose_player(home,'defense','control')
                             print('Ball goes to '+active_player['fam'])
                         else:
                             control=1
                             print('Attack is not over. Attackers takes the ball')
                             active_player=choose_player(away,'attack','control')
                             print('Ball goes to '+active_player['fam'])
                     elif roll<=defense/6:
                         #ball='homecorner'
                         ball='homezone'
                         print('But defender saves to the corner')
                         control=0
                         active_player=choose_player(home,'defense','control')
                         print('Ball goes to '+active_player['fam'])
                     elif roll<=defense/4:
                         print('But defenser saves! Ball flies back to the box')
                         ball='homebox'
                         #Расчет подбора мяча
                         defense=defense_streight(home)
                         attack=attack_streight(away)
                         roll=randint(0,defense+attack)
                         print('The Roll is '+str(roll)+'(0-'+str(defense)+' - Defense,'+str(defense)+'-'+str(defense+attack)+' - Attack)')
                         if roll<=defense:
                             control=0
                             print('Defenders takes the ball')
                             active_player=choose_player(home,'defense','control')
                             print('Ball goes to '+active_player['fam'])
                         else:
                             control=1
                             print('Another chance. Attackers takes the ball')
                             active_player=choose_player(away,'attack','control')
                             print('Chance for '+active_player['fam'])
                     else:
                         print('and it is a Goal!')
                         away_score+=1
                         ball='midfield'
                         control=0
                         print('Score is '+str(home_score)+':'+str(away_score))
                         active_player=choose_player(home,'midfield','control')    
                 else:    
                     print('and it is a Goal!')
                     print(opp_player['fam']+" can't stop the ball!")
                     away_score+=1
                     ball='midfield'
                     control=0
                     print('Score is '+str(home_score)+':'+str(away_score))
                     active_player=choose_player(home,'midfield','control')
             else:
                  print('But ball goes wide')
                  print('It is a goal kick for CSKA')
                  ball='homezone'
                  control=0
                  active_player=choose_player(home,'defense','control')
                  print('Ball goes to '+active_player['fam'])
                  
#Processing match situation in awaybox zone
    elif ball=='awaybox':
         if control==1:
             if active_player['pos']=='GK':
                 print(away_info['name']+' goalkeeper with the ball')    
                 opp_player=choose_player(home,'attack','pressing')
                 roll=randint(0, active_player['gk']+opp_player['def'])
                 print('The Roll is '+str(roll)+'(0-'+str(opp_player['def'])+' - Loose ball,'+str(opp_player['def'])+'-'+str(active_player['gk']+opp_player['def'])+' - Pass Forward)')
                 if roll<=opp_player['def']:
                     print('And.....he loses the ball to the attackers')
                     control=0
                     active_player=opp_player
                     print('A goal chance for '+active_player['fam']+'!!!')
                 else:
                     print('And he succesefully passes the ball to defenders')
                     ball='awayzone'
                     active_player=choose_player(away,'defense','control')
                     print('Ball goes forward to '+active_player['fam'])
             else:
                 print(active_player['fam']+' with the ball')    
                 opp_player=choose_player(home,'attack','pressing')
                 roll=randint(0, active_player['gk']+opp_player['def'])
                 print('The Roll is '+str(roll)+'(0-'+str(opp_player['def'])+' - Loose ball,'+str(opp_player['def'])+'-'+str(active_player['gk']+opp_player['def'])+' - Pass Forward)')
                 if roll<=opp_player['def']:
                     print('And.....he loses the ball to the attackers')
                     control=0
                     active_player=opp_player
                     print('A goal chance for '+active_player['fam']+'!!!')
                 else:
                     print('And he succesefully clears the ball to teammates')
                     ball='awayzone'
                     active_player=choose_player(away,'defense','control')
                     print('Ball goes forward to '+active_player['fam'])
         else:
             print('He shoots....')
             if active_player['att']<=90:
                 roll=randint(0,100)
                 print('The Roll is '+str(roll)+'(0-'+str(active_player['att'])+' - to the Goal,'+str(active_player['att'])+'-'+str(100)+' - Wide)')
             else:
                 roll=randint(0,active_player['att']+10)
                 print('The Roll is '+str(roll)+'(0-'+str(active_player['att'])+' - to the Goal,'+str(active_player['att'])+'-'+str(active_player['gk']+10)+' - Wide)')
             if roll<=active_player['att']:
                 print('Ball flies to the goal....')
                 opp_player=away[0]
                 #Расчет вариантов при попадании в ворота   
                 roll=randint(0,opp_player['gk']+active_player['att'])
                 print('The Roll is '+str(roll)+'(0-'+str(opp_player['gk']//2)+' - Save,'+str(opp_player['gk']//2)+'-'+str(opp_player['gk'])+' - Turn Out,'+str(opp_player['gk'])+'-'+str(opp_player['gk']+active_player['att']//2)+' - Do not reach out,'+str(opp_player['gk']+active_player['att']//2)+'-'+str(opp_player['gk']+active_player['att'])+' - Goal)')    
                 if roll<=opp_player['gk']//2:
                     print('but '+opp_player['fam']+' saves it!')
                     control=1
                     ball='awayzone'
                     print('He throw the ball to defenders')
                     active_player=choose_player(home,'defense','control')
                     print(active_player['fam']+'with the ball')
                 elif roll<=opp_player['gk']:
                     print(opp_player['fam']+' turn the ball out!')
                     #Расчет вариантов отскока мяча
                     roll=randint(0,opp_player['gk']+active_player['att'])
                     print('The Roll is '+str(roll)+'(0-'+str(opp_player['gk']//2)+' - Out of the box,'+str(opp_player['gk']//2)+'-'+str(opp_player['gk'])+' - Corner,'+str(opp_player['gk'])+'-'+str(opp_player['gk']+active_player['att']//2)+' - To the box,'+str(opp_player['gk']+active_player['att']//2)+'-'+str(opp_player['gk']+active_player['att'])+' - to the goal)')    
                     if roll<=opp_player['gk']//2:
                         print('Ball flies away from the box')
                         ball='awayzone'
                         #Расчет подбора мяча
                         defense=defense_streight(away)
                         attack=attack_streight(home)
                         roll=randint(0,defense+attack)
                         print('The Roll is '+str(roll)+'(0-'+str(defense)+' - Defense,'+str(defense)+'-'+str(defense+attack)+' - Attack)')
                         if roll<=defense:
                             control=1
                             print('Defenders takes the ball')
                             active_player=choose_player(away,'defense','control')
                             print('Ball goes to '+active_player['fam'])
                         else:
                             control=0
                             print('Attack is not over. Attackers takes the ball')
                             active_player=choose_player(home,'attack','control')
                             print('Ball goes to '+active_player['fam'])
                     elif roll<=opp_player['gk']:
                         #ball='awaycorner'
                         ball='awayzone'
                         print('Ball goes to corner')
                         control=1
                         active_player=choose_player(away,'defense','control')
                         print('Ball goes to '+active_player['fam'])
                     elif roll<=opp_player['gk']+active_player['att']//2:
                         print('Ball flies to the box')
                         ball='awaybox'
                         #Расчет подбора мяча
                         defense=defense_streight(away)
                         attack=attack_streight(home)
                         roll=randint(0,defense+attack)
                         print('The Roll is '+str(roll)+'(0-'+str(defense)+' - Defense,'+str(defense)+'-'+str(defense+attack)+' - Attack)')
                         if roll<=defense:
                             control=1
                             print('Defenders takes the ball')
                             active_player=choose_player(away,'defense','control')
                             print('Ball goes to '+active_player['fam'])
                         else:
                             control=0
                             print('Another chance. Attackers takes the ball')
                             active_player=choose_player(home,'attack','control')
                             print('Chance for '+active_player['fam'])
                     else:
                         print('But the ball falls to the goal by the hand of the goalkeeper')
                         home_score+=1
                         ball='midfield'
                         control=1
                         print('Score is '+str(home_score)+':'+str(away_score))
                         active_player=choose_player(away,'midfield','control')
                 elif roll<=opp_player['gk']+active_player['att']//2:
                     print(opp_player['fam']+' do not reach out the ball')
                     #Расчет вариантов, когда вратать обыгран
                     defense=defense_streight(away)
                     roll=randint(0,defense//4+active_player['att'])
                     print('The Roll is '+str(roll)+'(0-'+str(defense/12)+' - Out of the box,'+str(defense/12)+'-'+str(defense/6)+' - To the corner,'+str(defense/6)+'-'+str(defense/4)+' - To the box,'+str(defense/4)+'-'+str(defense/4+active_player['att'])+' - To the Goal)')
                     if roll<=defense/12:
                         print('But defender clears it out of the box')
                         ball='awayzone'
                         #Расчет подбора мяча
                         defense=defense_streight(away)
                         attack=attack_streight(home)
                         roll=randint(0,defense+attack)
                         print('The Roll is '+str(roll)+'(0-'+str(defense)+' - Defense,'+str(defense)+'-'+str(defense+attack)+' - Attack)')
                         if roll<=defense:
                             control=1
                             print('Defenders takes the ball')
                             active_player=choose_player(away,'defense','control')
                             print('Ball goes to '+active_player['fam'])
                         else:
                             control=0
                             print('Attack is not over. Attackers takes the ball')
                             active_player=choose_player(home,'attack','control')
                             print('Ball goes to '+active_player['fam'])
                     elif roll<=defense/6:
                         #ball='awaycorner'
                         ball='awayzone'
                         print('But defender saves to the corner')
                         control=1
                         active_player=choose_player(away,'defense','control')
                         print('Ball goes to '+active_player['fam'])
                     elif roll<=defense/4:
                         print('But defenser saves! Ball flies back to the box')
                         ball='awaybox'
                         #Расчет подбора мяча
                         defense=defense_streight(away)
                         attack=attack_streight(home)
                         roll=randint(0,defense+attack)
                         print('The Roll is '+str(roll)+'(0-'+str(defense)+' - Defense,'+str(defense)+'-'+str(defense+attack)+' - Attack)')
                         if roll<=defense:
                             control=1
                             print('Defenders takes the ball')
                             active_player=choose_player(away,'defense','control')
                             print('Ball goes to '+active_player['fam'])
                         else:
                             control=0
                             print('Another chance. Attackers takes the ball')
                             active_player=choose_player(home,'attack','control')
                             print('Chance for '+active_player['fam'])
                     else:
                         print('and it is a Goal!')
                         home_score+=1
                         ball='midfield'
                         control=1
                         print('Score is '+str(home_score)+':'+str(away_score))
                         active_player=choose_player(away,'midfield','control')    
                 else:    
                     print('and it is a Goal!')
                     print(opp_player['fam']+" can't stop the ball!")
                     home_score+=1
                     ball='midfield'
                     control=1
                     print('Score is '+str(home_score)+':'+str(away_score))
                     active_player=choose_player(away,'midfield','control')
             else:
                  print('But ball goes wide')
                  print('It is a goal kick for Ural')
                  ball='awayzone'
                  control=1
                  active_player=choose_player(away,'defense','control')
                  print('Ball goes to '+active_player['fam'])
    if time==90:
        print('Half time')
        print('Half time score is '+str(home_score)+':'+str(away_score))
    elif time==180:
        print('Full time')
        print('Full time score is '+str(home_score)+':'+str(away_score))
    input('Press ENTER\n')
    print('****************************************************************')
