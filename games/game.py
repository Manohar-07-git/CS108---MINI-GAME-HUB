import pygame 
import subprocess
import numpy as np
from games.tictactoe import TicTacToe 
from games.connect4 import c4
from games.othello import othello
from baseclass import base
import sys
import pathlib as Path 

p1=sys.argv[1]
p2=sys.argv[2]

def ask_continue():
    print("\n" + "="*50)
    print("  GAME OVER — What would you like to do next?")
    print("="*50)
    while True:
        choice = input("  Enter 'c' to play another game, or 'q' to quit: ").strip().lower()
        if choice == 'c':
            print("  Returning to the Game Hub menu...\n")
            return True
        elif choice == 'q':
            print("  Thanks for playing! Goodbye.\n")
            return False
        else:
            print("  Invalid input. Please enter 'c' to continue or 'q' to quit.")

########################################################## MAIN MENU ###############################################################################################
pygame.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption("GAME HUB!!!")
clock=pygame.time.Clock()

finalbg=pygame.image.load('media/final_bg.png').convert()
finalbg=pygame.transform.scale(finalbg,(1000,800))

bg_surf=pygame.image.load('media/menu_bg.png').convert()
bg_surf=pygame.transform.scale(bg_surf,(1000,800))

tic_surf=pygame.image.load('media/tictactoe.png').convert()
tic_surf=pygame.transform.scale(tic_surf,(200,200))
tic_rect=tic_surf.get_rect(topleft=(125,400))

oth_surf=pygame.image.load('media/othello.png')
oth_surf=pygame.transform.scale(oth_surf,(200,200))
oth_rect=oth_surf.get_rect(topleft=(375,400))

c4_surf=pygame.image.load('media/connect4.png').convert()
c4_surf=pygame.transform.scale(c4_surf,(200,200))
c4_rect=c4_surf.get_rect(topleft=(625,400))

font=pygame.font.Font(None, 100)
text=font.render("GAME HUB", False,(0,255,255))
text_rect=text.get_rect(center=(500,300))

######################################################################################################################################################################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

################################################### TIC TAC TOE ######################################################################################################################################
            if tic_rect.collidepoint(mouse_pos): 
                screen=pygame.display.set_mode((1000,800))
                pygame.display.set_caption("TIC TAC TOE")
                clock=pygame.time.Clock()

                player=base(p1,p2,10)
                tic=TicTacToe()
                
                ticbg=pygame.image.load('media/tictactoe_bg.png').convert()
                ticbg=pygame.transform.scale(ticbg,(1000,800))

                empty_surf=pygame.image.load('media/ticempty.png').convert()
                empty_surf=pygame.transform.scale(empty_surf,(80,80))

                x_surf=pygame.image.load('media/x.png').convert()
                x_surf=pygame.transform.scale(x_surf,(80,80))

                o_surf=pygame.image.load('media/o.png').convert()
                o_surf=pygame.transform.scale(o_surf,(80,80))

                x_rect=[]
                surf=[]

                for j in range(10):
                    xv_rect=[]
                    surfv=[]
                    for i in range(10):
                        rect_x=x_surf.get_rect(topleft=(j*80,i*80))
                        xv_rect.append(rect_x)
                        surfv.append(empty_surf)
                    x_rect.append(xv_rect)
                    surf.append(surfv)

                recorded = False 

######################################################################################################################################################################################################
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        if event.type == pygame.MOUSEBUTTONDOWN and tic.wincond(player.board,3-player.turn)==0:
                            mouse_pos=pygame.mouse.get_pos()
                            for j in range(10):
                                for i in range(10):
                                    if x_rect[i][j].collidepoint(mouse_pos):
                                        if surf[i][j] is empty_surf:
                                            player.board[i,j]=player.turn
                                            if player.turn==1:
                                                surf[i][j]=x_surf
                                            else:
                                                surf[i][j]=o_surf
                                            player.switchturn()

                    if not tic.wincond(player.board,player.turn):
                        screen.blit(ticbg,(0,0))

                        for i in range(10):
                            for j in range(10):
                                screen.blit(surf[i][j],x_rect[i][j])
                                
                    winner = None
                    if tic.wincond(player.board, player.turn):
                        winner = player.turn
                    elif tic.wincond(player.board, 3-player.turn):
                        winner = 3-player.turn
                        
                    if winner==1:
                        screen.blit(finalbg,(0,0))
                        text = font.render(f"{p1} won", False,(0,255,255))
                        if not recorded:
                            player.record(p1,p2,"tictactoe")
                            recorded = True
                        text_rect=text.get_rect(center=(500,300))
                        screen.blit(text,text_rect)
                    elif winner==2:
                        screen.blit(finalbg,(0,0))
                        text = font.render(f"{p2} won", False,(0,255,255))
                        if not recorded:
                            player.record(p2,p1,"tictactoe")
                            recorded = True
                        text_rect=text.get_rect(center=(500,300))
                        screen.blit(text,text_rect)
                    elif not np.any(player.board==0):
                        screen.blit(finalbg,(0,0))
                        text = font.render(f"TIE", False,(0,255,255)) 
                        if not recorded:
                            player.record("Tie",p1,"tictactoe",p2)
                            recorded = True
                        text_rect=text.get_rect(center=(500,300))
                        screen.blit(text,text_rect)
                        
                        
                    if winner==1 or winner==2 or not np.any(player.board==0):
                        wins_surf=pygame.image.load('media/wins.png').convert()
                        wins_surf=pygame.transform.scale(wins_surf,(200,40))
                        losses_surf=pygame.image.load('media/losses.png').convert()
                        losses_surf=pygame.transform.scale(losses_surf,(200,40))
                        ratio_surf=pygame.image.load('media/ratio.png').convert()
                        ratio_surf=pygame.transform.scale(ratio_surf,(200,40))
                        
                        wins_rect=wins_surf.get_rect(topleft=(125,500))
                        losses_rect=losses_surf.get_rect(topleft=(425,500))
                        ratio_rect=ratio_surf.get_rect(topleft=(725,500))
                        
                        screen.blit(wins_surf,wins_rect)
                        screen.blit(losses_surf,losses_rect)
                        screen.blit(ratio_surf,ratio_rect)

                        play_again_surf = pygame.font.Font(None, 60).render("PLAY AGAIN", False, (50, 255, 50))
                        play_again_rect = play_again_surf.get_rect(center=(350, 650))
                        leave_surf = pygame.font.Font(None, 60).render("LEAVE", False, (255, 50, 50))
                        leave_rect = leave_surf.get_rect(center=(650, 650))
                        
                        screen.blit(play_again_surf, play_again_rect)
                        screen.blit(leave_surf, leave_rect)
                       
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos=pygame.mouse.get_pos()
                            if wins_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh wins", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break 
                                else:
                                    pygame.quit()
                                    exit()
                            if losses_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh losses", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break
                                else:
                                    pygame.quit()
                                    exit()
                            if ratio_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh ratio", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break
                                else:
                                    pygame.quit()
                                    exit()
                            if play_again_rect.collidepoint(mouse_pos):
                                break 
                            if leave_rect.collidepoint(mouse_pos):
                                pygame.quit()
                                exit() 

                    pygame.display.update()
                    clock.tick(60)

############################################# OTHELLO #######################################################################################################################################################
            if oth_rect.collidepoint(mouse_pos): 
                screen=pygame.display.set_mode((1000,800))
                pygame.display.set_caption("OTHELLO")
                clock=pygame.time.Clock()

                player=base(p1,p2,8)
                othell=othello(8)

                ticbg=pygame.image.load('./media/othellobg.png').convert()
                ticbg=pygame.transform.scale(ticbg,(1000,800))

                empty_surf=pygame.image.load('./media/emptyc4.png').convert()
                empty_surf=pygame.transform.scale(empty_surf,(80,80))

                x_surf=pygame.image.load('./media/oth1.png').convert()
                x_surf=pygame.transform.scale(x_surf,(80,80))

                o_surf=pygame.image.load('./media/oth2.png').convert()
                o_surf=pygame.transform.scale(o_surf,(80,80))

                n_surf=pygame.image.load('./media/o.png')
                n_surf=pygame.transform.scale(n_surf,(80,80))

                x_rect=[]
                surf=[]

                for j in range(8):
                    xv_rect=[]
                    surfv=[]
                    for i in range(8):
                        rect_x=x_surf.get_rect(topleft=(220+(8-i-1)*80,120+(8-j-1)*80))
                        xv_rect.append(rect_x)
                        surfv.append(empty_surf)
                    x_rect.append(xv_rect)
                    surf.append(surfv)
                    
                recorded = False 
                
###########################################################################################################################################################################################################
                while True:
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            exit()

                        if event.type==pygame.MOUSEBUTTONDOWN and othell.wincond(player.turn)==False:
                            mouse_pos=pygame.mouse.get_pos()
                            for j in range(8):
                                for i in range(8):
                                    if x_rect[i][j].collidepoint(mouse_pos):
                                        if othell.validmoves(player.turn)[i,j]==1:
                                            othell.makemove(i,j,player.turn)
                                            player.switchturn()

                                            for d in range(8):
                                                for s in range(8):
                                                    if othell.board[d,s]==1:
                                                        surf[d][s] = x_surf
                                                    if othell.board[d,s]==2:
                                                        surf[d][s] = o_surf

                    screen.blit(ticbg,(0,0))

                    for d in range(8):
                        for s in range(8):
                            if othell.board[d,s]==1:
                                surf[d][s]=x_surf
                            if othell.board[d,s]==2:
                                surf[d][s]=o_surf

                    for i in range(8):
                        for j in range(8):
                            screen.blit(surf[i][j],x_rect[i][j])

                    for i in range(8):
                        for j in range(8):
                            if othell.validmoves(player.turn)[i,j]==1:
                                screen.blit(n_surf,x_rect[i][j])
                                
                    winner = None
                    l1,l2=othell.count()
                    fonts=pygame.font.Font(None,100)
                    texts=fonts.render(f"player1 : {l1} player2 : {l2}",False,(255,255,255))
                    texts_rect=texts.get_rect(center=(500,100))
                    screen.blit(texts,texts_rect)
                    
                    if othell.wincond(player.turn):
                        a1,a2=othell.count()
                        if a1>a2:
                            winner=1
                        if a1<a2:
                            winner=2
                        if a1==a2:
                            winner=3
                            
                    if winner==1:
                        screen.blit(finalbg,(0,0))
                        text = font.render(f"{p1} won", False,(0,255,255))
                        if not recorded:
                            player.record(p1,p2,"othello")
                            recorded = True
                        text_rect=text.get_rect(center=(500,300))
                        screen.blit(text,text_rect)
                    elif winner==2:
                        screen.blit(finalbg,(0,0))
                        if not recorded:
                            player.record(p2,p1,"othello")
                            recorded = True
                        text = font.render(f"{p2} won", False,(0,255,255))                
                        text_rect=text.get_rect(center=(500,300))
                        screen.blit(text,text_rect)
                    elif winner==3:
                        screen.blit(finalbg,(0,0))
                        text = font.render(f"TIE", False,(0,255,255))        
                        text_rect=text.get_rect(center=(500,300))
                        screen.blit(text,text_rect)
                        if not recorded:
                            player.record("Tie",p1,"othello",p2)
                            recorded = True
                        
                        
                    if winner==1 or winner==2 or winner==3:
                        wins_surf=pygame.image.load('media/wins.png').convert()
                        wins_surf=pygame.transform.scale(wins_surf,(200,40))
                        losses_surf=pygame.image.load('media/losses.png').convert()
                        losses_surf=pygame.transform.scale(losses_surf,(200,40))
                        ratio_surf=pygame.image.load('media/ratio.png').convert()
                        ratio_surf=pygame.transform.scale(ratio_surf,(200,40))
                        
                        wins_rect=wins_surf.get_rect(topleft=(125,500))
                        losses_rect=losses_surf.get_rect(topleft=(425,500))
                        ratio_rect=ratio_surf.get_rect(topleft=(725,500))
                        
                        screen.blit(wins_surf,wins_rect)
                        screen.blit(losses_surf,losses_rect) 
                        screen.blit(ratio_surf,ratio_rect)

                        play_again_surf = pygame.font.Font(None, 60).render("PLAY AGAIN", False, (50, 255, 50))
                        play_again_rect = play_again_surf.get_rect(center=(350, 650))
                        leave_surf = pygame.font.Font(None, 60).render("LEAVE", False, (255, 50, 50))
                        leave_rect = leave_surf.get_rect(center=(650, 650))
                        
                        screen.blit(play_again_surf, play_again_rect)
                        screen.blit(leave_surf, leave_rect)
                       
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos=pygame.mouse.get_pos()
                            if wins_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh wins", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break
                                else:
                                    pygame.quit()
                                    exit()
                            if losses_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh losses", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break
                                else:
                                    pygame.quit()
                                    exit()
                            if ratio_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh ratio", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break
                                else:
                                    pygame.quit()
                                    exit()
                            if play_again_rect.collidepoint(mouse_pos):
                                break
                            if leave_rect.collidepoint(mouse_pos):
                                pygame.quit()
                                exit()
                            
                    pygame.display.update()
                    clock.tick(60)

############################################## CONNECT FOUR ##############################################################################################
            if c4_rect.collidepoint(mouse_pos):
                screen=pygame.display.set_mode((1000,800))
                pygame.display.set_caption("CONNECT 4")
                clock=pygame.time.Clock()

                player=base(p1,p2,7)
                connect=c4()

                ticbg=pygame.image.load('./media/connectbg.png').convert()
                ticbg=pygame.transform.scale(ticbg,(1000,800))

                empty_surf=pygame.image.load('./media/emptyc4.png').convert()
                empty_surf=pygame.transform.scale(empty_surf,(80,80))

                x_surf=pygame.image.load('./media/disc1.png').convert()
                x_surf=pygame.transform.scale(x_surf,(80,80))

                o_surf=pygame.image.load('./media/disc2.png').convert()
                o_surf=pygame.transform.scale(o_surf,(80,80))

                x_rect=[]
                surf=[]

                for j in range(7):
                    xv_rect=[]
                    surfv=[]
                    for i in range(7):
                        rect_x=x_surf.get_rect(topleft=(220+(7-i-1)*80,120+(7-j-1)*80))
                        xv_rect.append(rect_x)
                        surfv.append(empty_surf)
                    x_rect.append(xv_rect)
                    surf.append(surfv)

                recorded = False 
                
###################################################################################################################################################################################################################################################################
                while True:
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            exit()

                        if event.type==pygame.MOUSEBUTTONDOWN and connect.wincond(player.board,player.turn)==0:
                            mouse_pos=pygame.mouse.get_pos()
                            for j in range(7):
                                for i in range(7):
                                    if x_rect[i][j].collidepoint(mouse_pos):
                                        for h in range(i+1):
                                            if surf[h][j] is empty_surf:
                                                if player.turn==1:
                                                    surf[h][j]=x_surf
                                                    player.board[h][j]=1
                                                    player.switchturn()
                                                    break
                                                else:
                                                    surf[h][j]=o_surf
                                                    player.board[h][j]=2
                                                    player.switchturn()
                                                    break

                    screen.blit(ticbg,(0,0))

                    for i in range(7):
                        for j in range(7):
                            screen.blit(surf[i][j],x_rect[i][j])
                    winner = None
                    
                    if connect.wincond(player.board, player.turn):
                        winner = player.turn
                    elif connect.wincond(player.board, 3-player.turn):
                        winner = 3-player.turn
                        
                    if winner==1:
                        screen.blit(finalbg,(0,0))
                        text = font.render(f"{p1} won", False,(0,255,255))
                        if not recorded:
                            player.record(p1,p2,"connect4")
                            recorded = True
                        text_rect=text.get_rect(center=(500,300))
                        screen.blit(text,text_rect)
                    elif winner==2:
                        screen.blit(finalbg,(0,0))
                        text = font.render(f"{p2} won", False,(0,255,255))                
                        text_rect=text.get_rect(center=(500,300))
                        if not recorded:
                            player.record(p2,p1,"connect4")
                            recorded = True
                        screen.blit(text,text_rect)
                    elif not np.any(player.board==0):
                        screen.blit(finalbg,(0,0))
                        text = font.render(f"TIE", False,(0,255,255))        
                        text_rect=text.get_rect(center=(500,300))
                        screen.blit(text,text_rect)
                        if not recorded:
                            player.record("Tie",p1,"connect4",p2)
                            recorded = True
                        
                    if winner==1 or winner==2 or not np.any(player.board==0):
                        wins_surf=pygame.image.load('media/wins.png').convert()
                        wins_surf=pygame.transform.scale(wins_surf,(200,40))
                        losses_surf=pygame.image.load('media/losses.png').convert()
                        losses_surf=pygame.transform.scale(losses_surf,(200,40))
                        ratio_surf=pygame.image.load('media/ratio.png').convert()
                        ratio_surf=pygame.transform.scale(ratio_surf,(200,40))
                        
                        wins_rect=wins_surf.get_rect(topleft=(125,500))
                        losses_rect=losses_surf.get_rect(topleft=(425,500))
                        ratio_rect=ratio_surf.get_rect(topleft=(725,500))
                        
                        screen.blit(wins_surf,wins_rect)
                        screen.blit(losses_surf,losses_rect)
                        screen.blit(ratio_surf,ratio_rect)

                        play_again_surf = pygame.font.Font(None, 60).render("PLAY AGAIN", False, (50, 255, 50))
                        play_again_rect = play_again_surf.get_rect(center=(350, 650))
                        leave_surf = pygame.font.Font(None, 60).render("LEAVE", False, (255, 50, 50))
                        leave_rect = leave_surf.get_rect(center=(650, 650))
                        
                        screen.blit(play_again_surf, play_again_rect)
                        screen.blit(leave_surf, leave_rect)
                       
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos=pygame.mouse.get_pos()
                            if wins_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh wins", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break
                                else:
                                    pygame.quit()
                                    exit()
                            if losses_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh losses", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break
                                else:
                                    pygame.quit()
                                    exit()
                            if ratio_rect.collidepoint(mouse_pos):
                                subprocess.run("bash leaderboard.sh ratio", shell=True)
                                subprocess.run(["python3", "plot.py"])
                                if ask_continue():
                                    screen = pygame.display.set_mode((1000, 800))
                                    pygame.display.set_caption("GAME HUB!!!")
                                    break
                                else:
                                    pygame.quit()
                                    exit()
                            if play_again_rect.collidepoint(mouse_pos):
                                break 
                            if leave_rect.collidepoint(mouse_pos):
                                pygame.quit()
                                exit() 
                            
                    pygame.display.update()
                    clock.tick(60)

################################################################################################################################################################################################################################################################
    # Redraw the main menu if a user "Plays Again" and returns here
    screen.fill((0, 0, 0)) # Clear previous screen
    screen.blit(bg_surf,(0,0))
    screen.blit(tic_surf,tic_rect)
    screen.blit(oth_surf,oth_rect)
    screen.blit(c4_surf,c4_rect)
    screen.blit(text,text_rect)
    pygame.display.update()
    clock.tick(60)