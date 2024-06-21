from presenters.pvp import PlayerVsPlayerPresenter, LoadGamePvpPresenter
from presenters.pvc import PlayerVsComputerPresenter, LoadGamePvcPresenter
from view.view import View

if __name__ == "__main__":
    view = View()
    pvp_presenter = PlayerVsPlayerPresenter()
    pvp_load_game_presenter = LoadGamePvpPresenter()
    pvc_presenter = PlayerVsComputerPresenter()
    pvc_load_game_presenter = LoadGamePvcPresenter()

    while True:

        menu_input = view.print_menu()

        if menu_input == 1:
            pvp_presenter.play_pvp_game()
        elif menu_input == 2:
            pvc_presenter.play_pvc_game()
        elif menu_input == 3:
            pvp_load_game_presenter.play_loaded_game()
