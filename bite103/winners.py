games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def print_game_stats(games_won = games_won):
    for name, games in games_won.items():
        if games == 1:
            game = "game"
        else:
            game = "games"
            
        print(f"{name} has won {games} {game}")
            
        