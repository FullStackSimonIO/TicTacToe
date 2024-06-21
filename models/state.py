import json
import os


def save_game(filename, board, game, player_1, player_2):
    game_data = {
        'board': board.convert_board_to_json(),
        'game': game.convert_to_json(),
        'player_1': {
            'symbol': player_1.symbol
        },
        'player_2': {
            'symbol': player_2.symbol
        }
    }
    with open(filename, 'w') as f:
        json.dump(game_data, f)
    print(f"Game saved to {filename}")


def load_game(filename, board, game, player_1, player_2):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist")
        return
    with open(filename, 'r') as f:
        data = f.read().strip()
        if not data:
            print(f"File {filename} is empty")
            return
        game_data = json.loads(data)
    board.load_from_json(game_data['board'])
    game.load_from_json(game_data['game'])
    player_1.symbol = game_data['player_1']['symbol']
    player_2.symbol = game_data['player_2']['symbol']
    print(f"Game loaded from {filename}")
