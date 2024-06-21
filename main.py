from presenters.pvp import PlayerVsPlayerPresenter
from presenters.pvc import PlayerVsComputerPresenter
from view.view import View

if __name__ == "__main__":
    view = View()
    pvp_presenter = PlayerVsPlayerPresenter()
    pvc_presenter = PlayerVsComputerPresenter()

    while True:

        menu_input = view.print_menu()

        if menu_input == 1:
            action = input("choose action:")
            pvp_presenter.play_pvp_game()
        elif menu_input == 2:
            pvc_presenter.play_pvc_game()
        elif menu_input == 3:
            pass
