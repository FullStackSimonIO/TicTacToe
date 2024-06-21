import json


def save_game(filename, board, game, human_player, computer_player):
    game_data = {
        'board': board.convert_board_to_json(),
        'game': game.convert_to_json(),
        'human_player': {
            'symbol': human_player.symbol
        },
        'computer_player': {
            'symbol': computer_player.symbol
        }
    }
    with open(filename, 'w') as f:
        json.dump(game_data, f)
    print(f"Game saved to {filename}")


def load_game(filename, board, game, human_player, computer_player):
    with open(filename, 'r') as f:
        game_data = json.load(f)
    board.load_from_json(game_data['board'])
    game.load_from_json(game_data['game'])
    human_player.symbol = game_data['human_player']['symbol']
    computer_player.symbol = game_data['computer_player']['symbol']
    print(f"Game loaded from {filename}")
