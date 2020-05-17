import time
import sys
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.125)


def play_tic_tac_toe():
    
    bp1 = '_|_|_'
    bp2 = '_|_|_'
    bp3 = ' | |'
    bp1p1 = '_|'
    bp1p2 = '_|'
    bp1p3 = '_'
    bp2p1 = '_|'
    bp2p2 = '_|'
    bp2p3 = '_'
    bp3p1 = ' |'
    bp3p2 = ' |'
    bp3p3 = ''
    p1_hist = []
    p2_hist = []
    print(bp1)
    print(bp2)
    print(bp3)
    player1 = input('Who is X?')
    player2 = input('Who is O?')
    game_ovr = False
    cnt = 0
    while game_ovr == False and cnt < 9:
        
        
        #Start With Player 1
        player1_input = int(input('Which Cell Will You Place Your Marker, '+player1+'? 1,2,3 ==> Top, 4,5,6 ==> Middle, 7,8,9 ==> Bottom'))
        if player1_input == 1:
            bp1p1 = 'X|'
            p1_hist.append(player1_input)
            bp1 = bp1p1 + bp1p2 + bp1p3 
            print(bp1)
            print(bp2)
            print(bp3)

        if player1_input == 2:
            bp1p2 = 'X|'            
            p1_hist.append(player1_input)
            bp1 = bp1p1+bp1p2+bp1p3
            print(bp1)
            print(bp2)
            print(bp3)
        if player1_input == 3:
            bp1p3 = 'X'
            bp1 = bp1p1+bp1p2+bp1p3
            p1_hist.append(player1_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player1_input == 4:
            bp2p1 = 'X|'
            p1_hist.append(player1_input)
            bp2 = bp2p1+bp2p2+bp2p3
            print(bp1)
            print(bp2)
            print(bp3)
        if player1_input == 5:
            bp2p2 = 'X|'
            bp2 = bp2p1+bp2p2+bp2p3
            p1_hist.append(player1_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player1_input == 6:
            bp2p3 = 'X'
            bp2 = bp2p1+bp2p2+bp2p3
            p1_hist.append(player1_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player1_input == 7:
            bp3p1 = 'X|'
            bp3 = bp3p1+bp3p2+bp3p3
            p1_hist.append(player1_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player1_input == 8:
            bp3p2 = 'X|'
            bp3 = bp3p1+bp3p2+bp3p3
            p1_hist.append(player1_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player1_input == 9:
            bp3p3 = 'X'
            bp3 = bp3p1+bp3p2+bp3p3
            p1_hist.append(player1_input)
            print(bp1)
            print(bp2)
            print(bp3)
            
        p1_hist.sort()
        cnt += 1
        
        if all(x in p1_hist for x in [1,2,3]) == True:
            delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break
        if all(x in p1_hist for x in [4,5,6]) == True:
            delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break  
        if all(x in p1_hist for x in [7,8,9]) == True:
            delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break  
        if all(x in p1_hist for x in [1,4,7]) == True:
            delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break
        if all(x in p1_hist for x in [2,5,8]) == True:
            delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break 
        if all(x in p1_hist for x in [3,6,9]) == True:
            delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break
        if all(x in p1_hist for x in [1,5,9]) == True:
            delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break      
        if all(x in p1_hist for x in [3,5,7]) == True:
            delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break 
        if cnt == 9:
            if all(x in p1_hist for x in [1,2,3]) == True:
                delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break
            if all(x in p1_hist for x in [4,5,6]) == True:
                delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break  
            if all(x in p1_hist for x in [7,8,9]) == True:
                delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break  
            if all(x in p1_hist for x in [1,4,7]) == True:
                delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break
            if all(x in p1_hist for x in [2,5,8]) == True:
                delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break 
            if all(x in p1_hist for x in [3,6,9]) == True:
                delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break
            if all(x in p1_hist for x in [1,5,9]) == True:
                delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break      
            if all(x in p1_hist for x in [3,5,7]) == True:
                delay_print('And the winner is ...'+ player1+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break
            else:
                delay_print("It's a draw!!! Do you want to rematch? If yes, re-run the cell.")
                game_ovr = True
                break
        #Now Player 2
        player2_input = int(input('Which Cell Will You Place Your Marker, '+player2+'? 1,2,3 ==> Top, 4,5,6 ==> Middle, 7,8,9 ==> Bottom'))
        if player2_input == 1:
            bp1p1 = 'O|'
            bp1 = bp1p1 + bp1p2 + bp1p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player2_input == 2:
            bp1p2 = 'O|'
            bp1 = bp1p1+bp1p2+bp1p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player2_input == 3:
            bp1p3 = 'O'
            bp1 = bp1p1+bp1p2+bp1p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player2_input == 4:
            bp2p1 = 'O|'
            bp2 = bp2p1+bp2p2+bp2p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player2_input == 5:
            bp2p2 = 'O|'
            bp2 = bp2p1+bp2p2+bp2p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player2_input == 6:
            bp2p3 = 'O'
            bp2 = bp2p1+bp2p2+bp2p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player2_input == 7:
            bp3p1 = 'O|'
            bp3 = bp3p1+bp3p2+bp3p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player2_input == 8:
            bp3p2 = 'O|'
            bp3 = bp3p1+bp3p2+bp3p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        if player2_input == 9:
            bp3p3 = 'O'
            bp3 = bp3p1+bp3p2+bp3p3
            p2_hist.append(player2_input)
            print(bp1)
            print(bp2)
            print(bp3)
        p1_hist.sort()
        p2_hist.sort()
        
        cnt += 1
        
        if all(x in p2_hist for x in [1,2,3]) == True:
            delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break
        if all(x in p2_hist for x in [4,5,6]) == True:
            delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break  
        if all(x in p2_hist for x in [7,8,9]) == True:
            delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break  
        if all(x in p2_hist for x in [1,4,7]) == True:
            delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break
        if all(x in p2_hist for x in [2,5,8]) == True:
            delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break 
        if all(x in p2_hist for x in [3,6,9]) == True:
            delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break
        if all(x in p2_hist for x in [1,5,9]) == True:
            delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break     
        if all(x in p2_hist for x in [3,5,7]) == True:
            delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
            gameovr = True
            break 
        if cnt == 9:
            if all(x in p2_hist for x in [1,2,3]) == True:
                delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break
            if all(x in p2_hist for x in [4,5,6]) == True:
                delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break  
            if all(x in p2_hist for x in [7,8,9]) == True:
                delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break  
            if all(x in p2_hist for x in [1,4,7]) == True:
                delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break
            if all(x in p2_hist for x in [2,5,8]) == True:
                delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break 
            if all(x in p2_hist for x in [3,6,9]) == True:
                delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break
            if all(x in p2_hist for x in [1,5,9]) == True:
                delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break     
            if all(x in p2_hist for x in [3,5,7]) == True:
                delay_print('And the winner is ...'+ player2+ '!!! Congrats! Do you want to rematch? If yes, re-run the cell.')
                gameovr = True
                break 
            else:
                delay_print("It's a draw!!! Do you want to rematch? If yes, re-run the cell.")
                game_ovr = True
                break