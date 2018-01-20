# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:01:30 2018

@author: Anurag
"""

player_1 = [4,4,4,4,4,4]
player_2 = [4,4,4,4,4,4]

pot_1=0
pot_2=0

total = player_1 + [pot_1] + player_2 +[pot_2]


def game_status():
    print("")
    print("Current position")
    print("")
    print("")
    
    print("                ######## Player 2 ########")
    print("")      
    print("            Position | 6 | 5 | 4 | 3 | 2 | 1 |")
    print("            ----------------------------------")
    print("            Count    | " + ' | '.join('{}'.format(k) for k in player_2[::-1]) + " |")
    
    print("")
    print("Player 2 Pot                                  Player 1 Pot")
    print("     {0}                                             {1}".format(pot_2,pot_1))
    print("")
    
    print("               ######## Player 1 ########")
    print("")
    print("            Position | 1 | 2 | 3 | 4 | 5 | 6 |")
    print("            ----------------------------------")
    print("            Count    | " + ' | '.join('{}'.format(k) for k in player_1) + " |")
    print("")
    print("")

        
def print_winner(pot_1,pot_2):
    if pot_1>pot_2:
        print("")
        print("##########################################################")
        print("                Player 1 won!!                            ")
        print("##########################################################")
        print("")
    elif pot_2>pot_1:
        print("")
        print("##########################################################")
        print("                Player 2 won!!                            ")
        print("##########################################################")
        print("")
    else:
        print("")
        print("##########################################################")
        print("                It's a draw!!                            ")
        print("##########################################################")
        print("")



def getBet(p):
    bet = 0
    while (bet <= 0) or (bet > 6):
        try:
            bet = int(input("Player {0}, select a position from 1 - 6: ".format(p)))
        except ValueError:
            print("Try again")
            pass
    return bet

game_status()

game_cont = True
exit_loop_a = False
exit_loop_b = False

while game_cont == True:

    while exit_loop_a == False:
        z_a = [(a+1) for a,b in enumerate(player_1) if b==0]
        choice_a=0
        cond_a=0
        while cond_a==0:
            choice_a= getBet(1)
            if choice_a not in z_a:
                cond_a=1
        
        pos_game = total[choice_a-1]
        aa = choice_a
        total[aa-1] =0
        total_copy = total[:]
             
        for i in range(0,pos_game):
            if (aa+i)>12:
                aa = -i
            total[aa+i] += 1
            check_pot=aa+i
            
        if (0<=check_pot<=5) and (total_copy[check_pot]==0) and (total[check_pot]!=0) and (total[12-check_pot]!=0):
            total[6] += total[check_pot] + total[12-check_pot]
            total[check_pot]=0
            total[12-check_pot]=0
        
        player_1 = total[0:6]
        player_2 = total[7:13]
        
        pot_1=total[6]
        pot_2=total[13]
        
        game_status()
        
        if sum(player_1)==0 or sum(player_2)==0:
            print_winner(pot_1,pot_2)
            game_cont = False
            exit_loop_a = True
            exit_loop_b = True
        
        if (check_pot)!=6:
            break
    
    while exit_loop_b == False:
        z_b = [(a+1) for a,b in enumerate(player_2) if b==0]
        choice_b=0
        cond_b=0
        while cond_b==0:
            choice_b= getBet(2)
            if choice_b not in z_b:
                cond_b=1
        
        pos_game = total[7+choice_b-1]
        bb = choice_b
        total[7+bb-1] =0
        total_copy = total[:]
        
        for i in range(0,pos_game):
            if (7+bb+i)>13:
                bb = -i-7
            total[7+bb+i] += 1
            check_pot=7+bb+i
        
        if (7<=check_pot<=12) and (total_copy[check_pot]==0) and (total[check_pot]!=0) and (total[12-check_pot]!=0):
            total[13] += total[check_pot] + total[12-check_pot]
            total[check_pot]=0
            total[12-check_pot]=0
        
        player_1 = total[0:6]
        player_2 = total[7:13]
        
        pot_1=total[6]
        pot_2=total[13]
        
        game_status()
        
        if sum(player_1)==0 or sum(player_2)==0:
            print_winner(pot_1,pot_2)
            game_cont = False
            exit_loop_a = True
            exit_loop_b = True
            
        if (check_pot)!=13:
                break

key = input('Press any key to exit')