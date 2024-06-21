from presenters.pvp import PlayerVsPlayerPresenter
from presenters.pvc import PlayerVsComputerPresenter


class Presenter(PlayerVsPlayerPresenter, PlayerVsComputerPresenter):

    def __init__(self):
        super().__init__()

    def play(self):
        while True:
            menu_input = self.view.print_menu()

            if menu_input == 1:
                self.play_pvp_game()

            elif menu_input == 2:
                print("PVC")

            elif menu_input == 3:
                print("")

            elif menu_input == 4:
                print("")
