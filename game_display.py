"""
ASCII Art for game
"""
HR ="======================"
TAB = "    "
def game_screen(game, player_1, player_2):
    scores(game, player_1, player_2)
    board(player_1, player_2)
    in_game_menu()
def scores(game, player_1, player_2):
    scores = str(player_1.name)+":"+str(player_1.score)
    scores+= TAB+str(player_2.name)+":"+str(player_2.score)
    print(HR)
    print("Day: "+str(game.day))
    print(scores)
    print('')
    
def board(player_1, player_2):
    board=str(player_1.nation.name)+TAB+str(player_2.nation.name)+"\n"
    board+="Wealth:"+str(player_1.nation)+TAB+str(player_2.nation)+"\n"
    print(board)
    
def in_game_menu():
    print("Action[1]"+TAB+"Action[2]"+TAB+"End Game[0]")
        
